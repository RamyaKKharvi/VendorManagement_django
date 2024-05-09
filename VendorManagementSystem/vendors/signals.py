import datetime

from django.dispatch import Signal
from django.dispatch import receiver

from vendors.models import HistoricalPerformanceModel
from vendors.service import (
    calculate_average_response_time,
    calculate_on_time_delivery_rate,
    calculate_quality_rating_avg,
    calculate_fulfillment_rate,
)

vendor_signal = Signal()


@receiver(vendor_signal)
def re_calculate_average_response_time(sender, **kwargs):
    vendor_obj = kwargs.get("vendor")

    vendor_obj.on_time_delivery_rate = calculate_on_time_delivery_rate(
        vendor_id=vendor_obj.id
    )
    vendor_obj.quality_rating_avg = calculate_quality_rating_avg(
        vendor_id=vendor_obj.id
    )
    vendor_obj.average_response_time = calculate_average_response_time(
        vendor_id=vendor_obj.id
    )
    vendor_obj.fulfillment_rate = calculate_fulfillment_rate(vendor_id=vendor_obj.id)
    performance_obj = HistoricalPerformanceModel(
        vendor=vendor_obj,
        date=datetime.datetime.now(),
        on_time_delivery_rate=vendor_obj.on_time_delivery_rate,
        average_response_time=vendor_obj.average_response_time,
        quality_rating_avg=vendor_obj.quality_rating_avg,
        fulfillment_rate=vendor_obj.fulfillment_rate,
    )
    performance_obj.save()
    vendor_obj.save()
