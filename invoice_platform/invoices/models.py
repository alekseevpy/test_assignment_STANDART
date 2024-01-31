from django.db import models


class PaymentDetail(models.Model):
    """Модель Реквизитов."""

    PAYMENT_TYPES = (
        ("Карта", "Карта"),
        ("Счёт", "Счёт"),
    )

    ACCOUNT_OR_CARD_TYPES = (
        ("Дебетовая карта", "Дебетовая карта"),
        ("Кредитная карта", "Кредитная карта"),
        ("Овердрафтная карта", "Овердрафтная карта"),
        ("Предоплаченная карта", "Предоплаченная карта"),
        ("Расчетный счет", "Расчетный счет"),
        ("Депозитный счет", "Депозитный счет"),
        ("Кредитный счет", "Кредитный счет"),
        ("Валютный счет", "Валютный счет"),
    )

    payment_type = models.CharField(max_length=50, verbose_name="Тип платежа")
    account_or_card_type = models.CharField(
        max_length=50, verbose_name="Тип карты/счёта"
    )
    owner_name = models.CharField(max_length=50, verbose_name="ФИО")
    phone_number = models.CharField(
        max_length=50, verbose_name="Номер телефона"
    )
    limit_amount = models.PositiveIntegerField(verbose_name="Лимит")

    class Meta:
        verbose_name_plural = "Реквизиты"


class Status(models.Model):
    """Модель Статуса."""

    name = models.CharField(
        "Название", max_length=15, unique=True, default="Ожидает оплаты"
    )

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return f"{self.name}"


class Invoice(models.Model):
    """Модель Заявки."""

    amount = models.PositiveIntegerField(verbose_name="Сумма")
    payment_detail = models.ForeignKey(
        PaymentDetail,
        on_delete=models.CASCADE,
        related_name="invoice",
        verbose_name="Реквизиты",
    )
    status = models.ForeignKey(
        Status,
        default=1,
        related_name="invoice",
        verbose_name="Статус",
        on_delete=models.PROTECT,
        null=False,
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка на сумму {self.amount}. Детали: {self.payment_detail}"
