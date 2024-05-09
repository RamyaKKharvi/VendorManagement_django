from datetime import datetime
from vendors.models import VendorModel, PurchaseOrderModel
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, ViewSet
from vendors.serializers import (
    VendorModelSerializer,
    PurchaseOrderModelSerializer,
    VendorPerformanceModelSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from vendors.config import PurchaseOrderStatusChoices
from vendors.signals import vendor_signal


class VendorProfile(ModelViewSet):
    queryset = VendorModel.objects.all()
    serializer_class = VendorModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrder(ModelViewSet):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderModelSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class VendorPerformance(ReadOnlyModelViewSet):
    queryset = VendorModel.objects.all()
    serializer_class = VendorPerformanceModelSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PurchaseOrderAcknowledgment(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, **kwargs):
        po_id = kwargs.get("id")
        try:
            purchase_order = PurchaseOrderModel.objects.get(id=po_id)
            if purchase_order and not purchase_order.acknowledgment_date:
                purchase_order.acknowledgment_date = datetime.now()
                purchase_order.status = PurchaseOrderStatusChoices.COMPLETED.value
                purchase_order.save()
                vendor_signal.send(
                    sender=None,
                    vendor=purchase_order.vendor,
                )
                return Response(
                    data={"success": "Purchase order acknowledged"},
                    status=status.HTTP_200_OK,
                )
            return Response(
                data={"error": "Purchase order already acknowledged"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": "Purchase order was not found!!!"},
                status=status.HTTP_400_BAD_REQUEST,
            )
