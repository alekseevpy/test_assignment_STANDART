from django_seed import Seed
from faker import Faker
from invoices.models import PaymentDetail

seeder = Seed.seeder()
fake = Faker()


def seed_payment_details():
    for _ in range(110):
        payment_type = fake.random_element(elements=["Карта", "Счёт"])
        account_or_card_type = fake.random_element(
            elements=[
                "Дебетовая карта",
                "Кредитная карта",
                "Овердрафтная карта",
                "Предоплаченная карта",
                "Расчетный счет",
                "Депозитный счет",
                "Кредитный счет",
                "Валютный счет",
            ]
        )
        owner_name = fake.name()
        phone_number = fake.phone_number()
        limit_amount = fake.random_int(min=1000, max=10000)

        PaymentDetail.objects.create(
            payment_type=payment_type,
            account_or_card_type=account_or_card_type,
            owner_name=owner_name,
            phone_number=phone_number,
            limit_amount=limit_amount,
        )


if __name__ == "__main__":
    seed_payment_details()
