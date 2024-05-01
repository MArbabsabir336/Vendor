from django.utils import timezone
from django.db import models
from django.db.models import Avg, F

from Utility.models import *

# Create your models here.
class VendorModel(CommonField):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.name
class PurchaseOrder(CommonField):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    
    po_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=50)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.po_number
    
class HistoricalPerformance(CommonField):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)

    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"