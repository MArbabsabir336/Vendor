from django.db.models import Count, Avg
from Vendorstore.models import *

def calculate_performance_metrics(vendor):
    completed_orders = vendor.purchaseorder_set.filter(status='completed')
    total_completed_orders = completed_orders.count()

    # performance metrics that are calculated as a ratio of completed orders
    if total_completed_orders > 0:
        vendor.on_time_delivery_rate = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count() / total_completed_orders
        vendor.quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg']
        vendor.average_response_time = completed_orders.exclude(acknowledgment_date=None).aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg']
        vendor.fulfillment_rate = completed_orders.filter(status='completed', quality_rating__isnull=False).count() / total_completed_orders
        vendor.save()
    else:
        vendor.on_time_delivery_rate = 0
        vendor.quality_rating_avg = 0
        vendor.average_response_time = 0
        vendor.fulfillment_rate = 0
        vendor.save()