from invoices.models import Invoice, PaymentDetail
from rest_framework import serializers


class PaymentDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для Реквизитов."""

    class Meta:
        model = PaymentDetail
        fields = (
            "id",
            "payment_type",
            "account_or_card_type",
            "owner_name",
            "phone_number",
            "limit_amount",
        )


class InvoiceSerializer(serializers.ModelSerializer):
    """Сериализатор для Заявки."""

    payment_detail = PaymentDetailSerializer(many=False)

    class Meta:
        model = Invoice
        fields = ("id", "amount", "payment_detail")
