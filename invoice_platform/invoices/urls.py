from django.urls import path

from .views import (
    CreateInvoiceView,
    detail_invoice,
    index,
    index_details,
    index_statuses,
    search_details,
)

app_name = "invoices"

urlpatterns = [
    path("", index, name="index"),
    path("create/", CreateInvoiceView.as_view(), name="create_invoice"),
    path("invoice/<int:invoice_id>/", detail_invoice, name="detail_invoice"),
    path("detail/", index_details, name="index_details"),
    path("status/", index_statuses, name="index_statuses"),
    path("search/", search_details, name="search_details"),
]
