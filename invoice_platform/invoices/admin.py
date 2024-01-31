from django.contrib import admin

from .models import Invoice, PaymentDetail, Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Админка: Статус"""

    list_display = (
        "id",
        "name",
    )
    list_filter = ("name",)


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    """Админка: Заявка"""

    list_display = (
        "id",
        "amount",
        "payment_detail",
        "status",
        "pub_date",
    )
    list_filter = ("status",)
    list_editable = ("status",)


@admin.register(PaymentDetail)
class PaymentDetailAdmin(admin.ModelAdmin):
    """Админка: Реквизиты"""

    list_display = (
        "id",
        "payment_type",
        "account_or_card_type",
        "owner_name",
        "phone_number",
        "limit_amount",
    )
    list_filter = ("payment_type", "account_or_card_type", "owner_name")
    list_editable = ("payment_type", "account_or_card_type")
