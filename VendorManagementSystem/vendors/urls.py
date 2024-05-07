from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("vendors", viewset=views.VendorProfile, basename="vendor-profile")
router.register(
    "purchase_orders", viewset=views.PurchaseOrder, basename="purchase-order"
)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "vendors/<int:vendor_id>/performance/",
        views.VendorPerformance.as_view({"get": "retrieve"}),
    ),
]
