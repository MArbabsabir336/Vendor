from django.contrib import admin
from django.urls import path,include
from Vendorstore.views import *

urlpatterns = [
    # Vender ----------------
    path('vendors/', VendorSroreApiView.as_view()),
    path('vendors/<str:vendor_id>/', VendorSroreApiView.as_view()),

    # Purchase Order ----------------
    path('purchase_orders/', PurchaseOrderApiView.as_view()),
    path('purchase_orders/<int:po_id>/', PurchaseOrderApiView.as_view()),
    
    path('vendors/<str:vendor_id>/purchase_orders/', HistoricalPerformanceApiView.as_view()),
]
