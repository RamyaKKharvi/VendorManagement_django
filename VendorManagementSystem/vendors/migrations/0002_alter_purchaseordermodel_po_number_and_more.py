# Generated by Django 5.0.4 on 2024-05-07 07:41

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vendors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseordermodel",
            name="po_number",
            field=models.CharField(
                default=uuid.UUID("3f048247-1ac6-4a4e-afc6-37c1f5b34d67"),
                max_length=36,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="vendormodel",
            name="vendor_code",
            field=models.CharField(
                default=uuid.UUID("e2d45074-f856-4baf-b145-3379703308a8"),
                max_length=36,
                unique=True,
            ),
        ),
    ]
