from datetime import timedelta
from django.db.models import Count, Avg
from Vendorstore.models import *

def calculate_performance_metrics(vendor):
    completed_orders = vendor.purchaseorder_set.filter(status='completed')
    total_completed_orders = completed_orders.count()

    if total_completed_orders > 0:
        vendor.on_time_delivery_rate = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count() / total_completed_orders
        vendor.quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']
        average_response_time_result = completed_orders.exclude(acknowledgment_date=None).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))
        vendor.average_response_time =  average_response_time_result['avg_response_time']
        vendor.fulfillment_rate = completed_orders.filter(status='completed', quality_rating__isnull=False).count() / total_completed_orders
        vendor.save()
        
def calculate_average_response_time(vendor):
    completed_orders = vendor.purchaseorder_set.filter(status='completed', acknowledgment_date__isnull=False)
    if completed_orders.exists():
        average_response_time_result = completed_orders.exclude(acknowledgment_date=None).aggregate(avg_response_time=Avg(F('acknowledgment_date') - F('issue_date')))
        vendor.average_response_time = average_response_time_result['avg_response_time']
        vendor.save()