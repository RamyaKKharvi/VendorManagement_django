from rest_framework import serializers
from .models import VendorModel, PurchaseOrderModel, HistoricalPerformanceModel


class VendorSerializer(serializers.Serializer):
    class Meta:
        model = VendorModel
        fields = [
            "name",
            "contact_details",
            "address",
            "vendor_code",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]


class PurchaseOrderSerializer(serializers.Serializer):
    class Meta:
        model = PurchaseOrderModel
        fields = [
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


class HistoricalPerformanceSerializer(serializers.Serializer):
    class Meta:
        model = HistoricalPerformanceModel
        fields = [
            "vendor",
            "date",
            "on_time_delivery_rate",
            "quality_rating_avg",
            "average_response_time",
            "fulfillment_rate",
        ]
