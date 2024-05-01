from rest_framework import serializers
from Vendorstore.models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'