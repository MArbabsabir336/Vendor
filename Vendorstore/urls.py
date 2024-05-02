from django.contrib import admin
from django.urls import path,include
from Vendorstore.views import *

urlpatterns = [
    # Vender ----------------
    path('vendors/', VendorSroreApiView.as_view()),
    path('vendors/<str:vendor_id>/', VendorSroreApiView.as_view()),

    # Purchase Order ----------------
    path('purchase_orders/', PurchaseOrderApiView.as_view()),
    path('purchase_orders/<str:po_id>/', PurchaseOrderApiView.as_view()),
    
    path('vendors/<str:vendor_id>/performance/', VendorPerformanceApiView.as_view()),
    path('purchase_orders/<str:po_id>/acknowledge/', AcknowledgePurchaseOrderApiView.as_view()),
    path('Vendors/<str:vendor_id>/historical_performance/', HistoricalPerformanceApiView.as_view()),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
