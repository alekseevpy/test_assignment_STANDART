from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from invoice_platform.settings import NUMBER_INVOICES

from .forms import InvoiceForm, PaymentDetailForm
from .models import Invoice, PaymentDetail, Status


def get_paginator(invoices, request):
    """Пагинатор"""
    page_number = request.GET.get("page", 1)
    paginator = Paginator(invoices, NUMBER_INVOICES)
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    template = "invoices/index.html"
    invoices = Invoice.objects.all()
    context = {
        "page_obj": get_paginator(invoices, request),
    }
    return render(request, template, context)


@login_required
def index_details(request):
    template = "details/index_detail.html"
    details = PaymentDetail.objects.all()
    context = {
        "page_obj": get_paginator(details, request),
    }
    return render(request, template, context)


def search_details(request):
    query = request.GET.get("q", "")

    if query:
        details = PaymentDetail.objects.filter(
            Q(payment_type__icontains=query)
            | Q(account_or_card_type__icontains=query)
            | Q(owner_name__icontains=query)
            | Q(phone_number__icontains=query)
        ).order_by("id")
    else:
        details = PaymentDetail.objects.all()

    context = {
        "details": details,
        "query": query,
    }

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(request, "details/search_results.html", context)
    else:
        return render(request, "details/search_results.html", context)


@user_passes_test(lambda user: user.is_staff or user.is_superuser)
def index_statuses(request):
    template = "statuses/index_status.html"
    statuses = Status.objects.all()
    context = {
        "page_obj": get_paginator(statuses, request),
    }
    return render(request, template, context)


class CreateInvoiceView(View):
    template = "invoices/create_invoice.html"

    def get(self, request, *args, **kwargs):
        invoice_form = InvoiceForm()
        payment_detail_form = PaymentDetailForm()
        return render(
            request,
            self.template,
            {
                "invoice_form": invoice_form,
                "payment_detail_form": payment_detail_form,
            },
        )

    def post(self, request, *args, **kwargs):
        invoice_form = InvoiceForm(request.POST)
        payment_detail_form = PaymentDetailForm(request.POST)

        if invoice_form.is_valid() and payment_detail_form.is_valid():
            payment_detail = payment_detail_form.save()
            invoice = Invoice(
                amount=invoice_form.cleaned_data["amount"],
                payment_detail=payment_detail,
            )
            invoice.save()

            return redirect("/")

        return render(
            request,
            self.template,
            {
                "invoice_form": invoice_form,
                "payment_detail_form": payment_detail_form,
            },
        )


def detail_invoice(request, invoice_id):
    """Информация о Заявке"""
    template = "invoices/detail_invoice.html"
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    context = {
        "invoice": invoice,
    }
    return render(request, template, context)
