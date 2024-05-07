from django.db.models import TextChoices


class PurchaseOrderStatusChoices(TextChoices):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
