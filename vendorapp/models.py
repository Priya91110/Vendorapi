"""To get ModelSerializer"""
from rest_framework import serializers
from django.db import models


class VendorModel(models.Model):
    name = models.CharField(max_length=225) 
    contact_details = models.TextField()
    address = models.TextField() 
    vendor_code = models.CharField(max_length=225)
    on_time_delivery_rate = models.FloatField() 
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField() 
    fulfillment_rate = models.FloatField()
    
    def __str__(self):
        return f"Vendor Name:- {self.name}/ Contact :- {self.contact_details}"
    
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = "__all__" 
        
        
class PurchaseOrderModel(models.Model):
    po_number = models.CharField(max_length=225)
    vendor = models.ForeignKey(VendorModel,related_name='purchase_orders', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField() 
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ])
    quality_rating = models.FloatField(null=True, blank=True) 
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True) 
    
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderModel
        fields = "__all__"
        
"""        
This model optionally stores historical data on vendor performance, enabling trend analysis.
"""            
class HistoricalPerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"Historical Performance of {self.vendor.name} on {self.date}"


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformanceModel
        fields = '__all__'