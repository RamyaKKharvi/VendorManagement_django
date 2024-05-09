import random

from django.db import models
from vendors.config import PurchaseOrderStatusChoices


def get_unique_vender_code():
    return f"VN-{str(random.randint(1, 10000)).zfill(3)}{str(random.randint(1, 1000)).zfill(3)}"


def get_unique_po_number():
    return (
        f"PO-{str(random.randint(1, 10000)).zfill(3)}-{str(random.randint(1, 10000)).zfill(3)}-{str(random.randint(1, 10000)).zfill(3)}",
    )


class VendorModel(models.Model):
    name = models.CharField(max_length=200)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(
        max_length=16,
        editable=False,
        unique=True,
        default=get_unique_vender_code,
    )
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)


class PurchaseOrderModel(models.Model):
    po_number = models.CharField(
        max_length=25,
        editable=False,
        default=get_unique_po_number,
        unique=True,
    )
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField(default=0)
    status = models.CharField(
        max_length=50,
        choices=PurchaseOrderStatusChoices.choices,
        default=PurchaseOrderStatusChoices.PENDING.value,
    )
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)


class HistoricalPerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
