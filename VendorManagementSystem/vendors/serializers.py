from rest_framework import serializers
from vendors.models import VendorModel, PurchaseOrderModel
from vendors.config import PurchaseOrderStatusChoices
from vendors.signals import vendor_signal


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
            and validated_data["acknowledgment_date"] is not None
        ):
            super().update(instance, validated_data)

            vendor_signal.send(
                sender=None,
                vendor=instance.vendor,
            )

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
