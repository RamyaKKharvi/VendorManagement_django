from .models import PurchaseOrderModel
from django.db.models import F, Avg, Count, ExpressionWrapper, DurationField


def calculate_on_time_delivery_rate(vendor_id):
    completed_pos = PurchaseOrderModel.objects.filter(
        status="completed", vendor=vendor_id
    )
    total_completed_pos = completed_pos.count()
    if total_completed_pos > 0:
        on_time_count = completed_pos.filter(
            delivery_date__lte=F("acknowledgment_date")
        ).count()
        return (on_time_count / total_completed_pos) * 100
    else:
        return 0


def calculate_quality_rating_avg(vendor_id):
    quality_rating_avg = (
        PurchaseOrderModel.objects.filter(
            quality_rating__isnull=False, vendor=vendor_id
        )
        .aggregate(avg_rating=Avg("quality_rating"))
        .get("avg_rating", 0)
    )
    return quality_rating_avg


def calculate_average_response_time(vendor_id):
    response_time = (
        PurchaseOrderModel.objects.filter(
            acknowledgment_date__isnull=False, vendor=vendor_id
        )
        .annotate(
            time_diff=ExpressionWrapper(
                F("acknowledgment_date") - F("issue_date"), output_field=DurationField()
            )
        )
        .aggregate(avg_response_time=Avg("time_diff"))
        .get("avg_response_time", 0)
    )
    if response_time:
        return response_time.total_seconds() / 3600  # Convert to hours
    else:
        return 0


def calculate_fulfillment_rate(vendor_id):
    total_pos = PurchaseOrderModel.objects.filter(
        status="completed", vendor=vendor_id
    ).count()
    if total_pos > 0:
        fulfilled_count = PurchaseOrderModel.objects.filter(status="completed").count()
        return (fulfilled_count / total_pos) * 100
    else:
        return 0
