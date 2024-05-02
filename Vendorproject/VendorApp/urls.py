from django.contrib import admin
from django.urls import path
from .views import(
    VendorView,
    PurchaseOrderView,
    HistoricalPerformanceView
)
urlpatterns = [
    path('vendor/',VendorView.as_view(),name="vender_view"),
    path('purchase_order/',PurchaseOrderView.as_view(),name="purchase_order_view"),
    path('historical_performance/',HistoricalPerformanceView.as_view(),name="historical_performance")
    
    
]
