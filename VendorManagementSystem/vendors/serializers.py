import datetime

from rest_framework import serializers
from vendors.models import VendorModel, PurchaseOrderModel, HistoricalPerformanceModel
from vendors.config import PurchaseOrderStatusChoices
from vendors.service import (
    calculate_on_time_delivery_rate,
    calculate_quality_rating_avg,
    calculate_average_response_time,
    calculate_fulfillment_rate,
)


class VendorModelSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.ReadOnlyField()
    quality_rating_avg = serializers.ReadOnlyField()
    average_response_time = serializers.ReadOnlyField()
    fulfillment_rate = serializers.ReadOnlyField()

    class Meta:
        model = VendorModel
        fields = [
            "id",
            "name",
            "contact_details",
            "address",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class PurchaseOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = [
            "id",
            "po_number",
            "vendor",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "quality_rating",
            "issue_date",
            "acknowledgment_date",
        ]

    def validate(self, attrs):
        return super().validate(attrs)

    def update(self, instance, validated_data):
        if (
            instance.status != validated_data["status"]
            and validated_data["status"] == PurchaseOrderStatusChoices.COMPLETED.value
        ):
            super().update(instance, validated_data)

            vendor_obj = instance.vendor
            vendor_obj.on_time_delivery_rate = calculate_on_time_delivery_rate(
                vendor_id=vendor_obj.id
            )
            vendor_obj.quality_rating_avg = calculate_quality_rating_avg(
                vendor_id=vendor_obj.id
            )
            vendor_obj.average_response_time = calculate_average_response_time(
                vendor_id=vendor_obj.id
            )
            vendor_obj.fulfillment_rate = calculate_fulfillment_rate(
                vendor_id=vendor_obj.id
            )
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

        else:
            super().update(instance, validated_data)

        return instance


class VendorPerformanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = [
            "id",
            "name",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
