from vendors.models import VendorModel, PurchaseOrderModel
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from vendors.serializers import (
    VendorModelSerializer,
    PurchaseOrderModelSerializer,
    VendorPerformanceModelSerializer,
)


class VendorProfile(ModelViewSet):
    queryset = VendorModel.objects.all()
    serializer_class = VendorModelSerializer


class PurchaseOrder(ModelViewSet):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderModelSerializer


class VendorPerformance(ReadOnlyModelViewSet):
    queryset = VendorModel.objects.all()
    serializer_class = VendorPerformanceModelSerializer
    lookup_field = "id"
