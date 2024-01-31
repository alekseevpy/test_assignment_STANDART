from django.core.management.base import BaseCommand
from invoices.models import Status


class Command(BaseCommand):
    help = "Заполнение статусов"

    def handle(self, *args, **options):
        statuses = [
            {"name": "Ожидает оплаты"},
            {"name": "Оплачена"},
            {"name": "Отменена"},
        ]

        for status_data in statuses:
            Status.objects.get_or_create(**status_data)

        self.stdout.write(self.style.SUCCESS("Статусы успешно заполнены"))
