from django.urls import path

from .views import InvoiceStatusView, create_invoice

app_name = "api"

urlpatterns = [
    path("api/create_invoice/", create_invoice, name="create_invoice"),
    path(
        "api/get_invoice_status/<int:invoice_id>/",
        InvoiceStatusView.as_view(),
        name="get_invoice_status",
    ),
]
