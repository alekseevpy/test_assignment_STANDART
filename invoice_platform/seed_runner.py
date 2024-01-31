import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "invoice_platform.settings")
django.setup()

from invoices.seed.invoice_seed import seed_invoices
from invoices.seed.payment_detail_seed import seed_payment_details
from invoices.seed.status_seed import Command as StatusSeeder

if __name__ == "__main__":
    seed_payment_details()
    seeder = StatusSeeder()
    seeder.handle()
    seed_invoices()
