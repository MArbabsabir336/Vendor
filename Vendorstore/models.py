from django.utils import timezone
from django.db import models
from django.db.models import Avg, F

# Create your models here.
class VendorModel(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def calculate_performance_metrics(self):
        # On-Time Delivery Rate
        completed_pos = self.purchaseorder_set.filter(status='completed')
        on_time_delivered_pos = completed_pos.filter(delivery_date__lte=timezone.now())
        on_time_delivery_rate = on_time_delivered_pos.count() / completed_pos.count()

        # Quality Rating Average
        quality_rating_avg = completed_pos.filter(quality_rating__isnull=False).aggregate(avg_quality=Avg('quality_rating'))['avg_quality']

        # Average Response Time
        response_times = completed_pos.exclude(acknowledgment_date=None).annotate(
            response_time=Avg(F('acknowledgment_date') - F('issue_date'))
        )
        average_response_time = response_times.aggregate(avg_response=Avg('response_time'))['avg_response']

        # Fulfilment Rate
        fulfillment_rate = completed_pos.filter(issues=None).count() / self.purchaseorder_set.count()

        return {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate
        }

class PurchaseOrder(models.Model):
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

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
