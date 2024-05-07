from .models import VendorModel, PurchaseOrderModel, HistoricalPerformanceModel
from rest_framework.viewsets import ViewSet
from .serializers import (
    VendorSerializer,
    PurchaseOrderSerializer,
    HistoricalPerformanceSerializer,
)
from rest_framework.response import Response
from rest_framework import status


class VendorProfile(ViewSet):
    def list(self, requests):
        try:
            vendors_list = VendorModel.objects.all()
            vendor_serializer = VendorSerializer(vendors_list, many=True)
            return Response(vendor_serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                data={"error": "server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def retrieve(self, requests, pk):
        try:
            vendor = VendorModel.objects.filter(id=pk).first()
            if vendor is not None:
                vendor_serializer = VendorSerializer(vendor)
                return Response(vendor_serializer.data, status=status.HTTP_200_OK)
            return Response(
                data={"error_message": "No Data Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception:
            return Response(
                data={"error": "server error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def create(self, requests):
        try:
            vendor_serializer = VendorSerializer(requests.data)
            if vendor_serializer.is_valid():
                vendor_serializer.save()
                return Response(
                    {"message": "Data Created Successfully"},
                    status=status.HTTP_201_CREATED,
                )
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, requests, pk):
        try:
            vendor = VendorModel.objects.filter(id=pk).first()
            if vendor is not None:
                vendor_serializer = VendorSerializer(vendor, data=requests.data)
                if vendor_serializer.is_valid():
                    vendor_serializer.save()
                    return Response(
                        {"message": "Complete Data Updated Successfully"},
                        status=status.HTTP_200_OK,
                    )
            else:
                return Response(
                    data={"error_message": "No Data Found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def partial_update(self, requests, pk):
        try:
            vendor = VendorModel.objects.get(id=pk)
            vendor_serializer = VendorSerializer(vendor, data=requests.data)
            if vendor_serializer.is_valid():
                vendor_serializer.save()
                return Response(
                    {"message": "Partial Data Updated Successfully"},
                    status=status.HTTP_200_OK,
                )
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, requests, pk):
        try:
            vendor = VendorModel.objects.get(id=pk)
            vendor.delete()
            return Response(
                {"message": "Vendor Data deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PurchaseOrder(ViewSet):
    def list(self, requests):
        try:
            purchase_order_list = PurchaseOrderModel.objects.all()
            purchase_order_serializer = PurchaseOrderSerializer(
                purchase_order_list, many=True
            )
            return Response(purchase_order_serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve(self, requests, pk):
        try:
            purchase_order = PurchaseOrderModel.objects.get(id=pk)
            purchase_order_serializer = PurchaseOrderSerializer(purchase_order)
            return Response(purchase_order_serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def create(self, requests):
        try:
            purchase_order_serializer = PurchaseOrderSerializer(data=requests.data)
            if purchase_order_serializer.is_valid():
                purchase_order_serializer.save()
                return Response(
                    {"message": "Data Created Successfully"},
                    status=status.HTTP_201_CREATED,
                )
        except:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def update(self, requests, pk):
        try:
            purchase_order = PurchaseOrderModel.objects.get(id=pk)
            purchase_order_serializer = PurchaseOrderSerializer(
                purchase_order, data=requests.data
            )
            if purchase_order_serializer.is_valid():
                purchase_order_serializer.save()
                return Response(
                    {"message": "Complete Data Updated Successfully"},
                    status=status.HTTP_200_OK,
                )
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def partial_update(self, requests, pk):
        try:
            purchase_order = PurchaseOrderModel.objects.get(id=pk)
            purchase_order_serializer = PurchaseOrderSerializer(
                purchase_order, data=requests.data
            )
            if purchase_order_serializer.is_valid():
                purchase_order_serializer.save()
                return Response(
                    {"message": "Partial Data Updated Successfully"},
                    status=status.HTTP_200_OK,
                )
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, requests, pk):
        try:
            purchase_order = PurchaseOrderModel.objects.get(id=pk)
            purchase_order.delete()
            return Response(
                {"message": "Data Deleted Successfully"}, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class VendorPerformance(ViewSet):

    def retrieve(self, requests, vendor_id):
        print("vendor id", vendor_id)
        try:
            vendor_performance = HistoricalPerformanceModel.objects.get(id=vendor_id)
            performance_serializer = HistoricalPerformanceSerializer(vendor_performance)
            return Response(performance_serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {"error": "server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
