from django.contrib import admin
from Vendorstore.models import *
# Register your models here.

@admin.register(VendorModel)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'vendor_code', 'contact_details', 'address', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
    search_fields = ['name', 'contact_details', 'vendor_code']
    
@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_number', 'vendor', 'order_date', 'status', 'delivery_date', 'items', 'quantity', 'quality_rating', 'issue_date', 'acknowledgment_date']
    search_fields = ['po_number', 'vendor__name']
    
@admin.register(HistoricalPerformance)
class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
    search_fields = ['vendor__name']