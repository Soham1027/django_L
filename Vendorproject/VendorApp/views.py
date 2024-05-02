from django.shortcuts import render
from rest_framework import generics
from .models import (
    Vendor,
    PurchaseOrder,
    HistoricalPerformance
)
from .serializer import (
    VendorSerializer,
    PurchaseOrderSerializer,
    HistoricalPerformanceSerializer
)

# Create your views here.

class VendorView(generics.ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

class PurchaseOrderView(generics.ListCreateAPIView):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer

class HistoricalPerformanceView(generics.ListCreateAPIView):
    queryset=HistoricalPerformance.objects.all()
    serializer_class=HistoricalPerformanceSerializer

