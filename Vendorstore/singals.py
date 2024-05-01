from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from Vendorstore.models import *
from Vendorstore.logic import *

@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    calculate_performance_metrics(instance.vendor)


@receiver(post_save, sender=PurchaseOrder)    
def save_historical_performance(sender, instance, **kwargs):
    HistoricalPerformance.objects.create(
        vendor=instance.vendor,
        date=instance.delivery_date,
        on_time_delivery_rate=instance.vendor.on_time_delivery_rate,
        quality_rating_avg=instance.vendor.quality_rating_avg,
        average_response_time=instance.vendor.average_response_time,
        fulfillment_rate=instance.vendor.fulfillment_rate
    )