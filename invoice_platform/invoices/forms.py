from django import forms

from .models import Invoice, PaymentDetail


class InvoiceForm(forms.ModelForm):
    amount = forms.IntegerField(
        label="Сумма",
        required=True,
    )

    class Meta:
        model = Invoice
        fields = ["amount"]


class PaymentDetailForm(forms.ModelForm):
    payment_type = forms.ChoiceField(
        choices=PaymentDetail.PAYMENT_TYPES,
        label="Тип платежа",
        required=True,
    )
    account_or_card_type = forms.ChoiceField(
        choices=PaymentDetail.ACCOUNT_OR_CARD_TYPES,
        label="Тип карты/счёта",
        required=True,
    )
    owner_name = forms.CharField(
        max_length=255,
        label="ФИО",
        required=True,
    )
    phone_number = forms.CharField(
        max_length=15,
        label="Номер телефона",
        required=True,
    )
    limit_amount = forms.IntegerField(
        label="Лимит",
        required=True,
    )

    class Meta:
        model = PaymentDetail
        fields = [
            "payment_type",
            "account_or_card_type",
            "owner_name",
            "phone_number",
            "limit_amount",
        ]
