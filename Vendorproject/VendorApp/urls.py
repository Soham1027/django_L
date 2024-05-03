from django.contrib import admin
from django.urls import path
from .views import(
    VendorView,
    PurchaseOrderView,
    HistoricalPerformanceView
)
urlpatterns = [
    path('vendors/',VendorView.as_view(),name="vender_view"),
    path('purchase_orders/',PurchaseOrderView.as_view(),name="purchase_order_view"),
    path('performance/',HistoricalPerformanceView.as_view(),name="historical_performance"),
  
  
    path('vendors/<int:pk>/',VendorView.as_view(),name="vender_view"),
    path('purchase_orders/<int:pk>/',PurchaseOrderView.as_view(),name="purchase_order_view"),
    path('performance/<int:pk>/',HistoricalPerformanceView.as_view(),name="historical_performance")
    
    
]
