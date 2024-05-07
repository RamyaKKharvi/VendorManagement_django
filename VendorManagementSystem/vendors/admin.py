from django.contrib import admin
from .models import VendorModel, PurchaseOrderModel, HistoricalPerformanceModel


@admin.register(VendorModel)
class VendorAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "contact_details",
        "address",
        "vendor_code",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    ]


@admin.register(PurchaseOrderModel)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = [
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


@admin.register(HistoricalPerformanceModel)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = [
        "vendor",
        "date",
        "on_time_delivery_rate",
        "quality_rating_avg",
        "average_response_time",
        "fulfillment_rate",
    ]
