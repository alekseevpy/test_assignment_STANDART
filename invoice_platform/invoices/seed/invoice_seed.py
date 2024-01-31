from django.utils import timezone
from django_seed import Seed
from faker import Faker
from invoices.models import Invoice, PaymentDetail, Status

seeder = Seed.seeder()
fake = Faker()


def seed_invoices():
    seeder.add_entity(
        Invoice,
        5500,
        {
            "amount": fake.random_int(min=100, max=10000),
            "payment_detail": lambda x: PaymentDetail.objects.order_by(
                "?"
            ).first(),
            "status": lambda x: Status.objects.order_by("?").first(),
            "pub_date": timezone.now(),
        },
    )
    seeder.execute()


if __name__ == "__main__":
    seed_invoices()
