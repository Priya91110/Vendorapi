from django.shortcuts import render
from .models import VendorModel, VendorSerializer, PurchaseOrderModel, PurchaseOrderSerializer, HistoricalPerformanceModel,  PerformanceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework import generics, mixins
from rest_framework.views import APIView
import datetime
from django.db.models import Avg , F
from django.utils import timezone
from datetime import timedelta
# Create your views here.
'''
list() -- get()--ListModelMixin
create --- post()-- CreateModelMixin
retrieve-- get()id--- RetrieveModelMixin
destroy-- delete()--- DestroyModelMixin
update --- put()-- UpdateModelMixin
'''


class getpostvendor(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    
class getputdelete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer
    
    """get handel request with id"""
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
      
    def delete(self, request, pk):
        return self.destroy(request, pk)
      

class PurchaseListCreate(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer
    
    def get(self, request):     
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
"""_
Track purchase orders with fields like PO number, vendor reference,
order date, items, quantity, and status.
"""


class PurchaseDetailView(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = PurchaseOrderModel.objects.all()
    serializer_class = PurchaseOrderSerializer
    
    """get handelar method and handel request with po id and retrieve() to retrieve data"""
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    """ put handelar method and handel request with po id and update() to update purchase detail """
    def put(self, request, pk):
        return self.update(request, pk)
    
    """ delete function fetchs detail about purchase model with po id and used destroy() to destroy order """        
    def delete(self, request, pk):
        return self.destroy(request, pk)
  
class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Vendor Name:- shyam lal/ Contact :- 952565325 
        performance_data = self.calculate_performance(instance)
        historical_data = HistoricalPerformanceModel.objects.filter(vendor=instance).order_by('-date')[:10]  # Change the limit as needed
        historical_serializer = PerformanceSerializer(historical_data, many=True)
        performance_data['historical_performance'] = historical_serializer.data
        return Response(performance_data)

    def calculate_performance(self, vendor):
        completed_orders = PurchaseOrderModel.objects.filter(vendor=vendor, status='completed')

        on_time_delivery_rate = (
            completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count() /
            completed_orders.count()
        ) if completed_orders.count() > 0 else 0.0

        quality_rating_avg = (
            completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
        )

        average_response_time = (
            completed_orders.filter(acknowledgment_date__isnull=False)
                           .aggregate(average_response=Avg(F('acknowledgment_date') - F('issue_date')))['average_response']
            or timedelta()
        ).total_seconds() / 3600  # in hours

        fulfillment_rate = (
            completed_orders.filter(status='completed', issue_date__isnull=True).count() /
            completed_orders.count()
        ) if completed_orders.count() > 0 else 0.0

        # Save historical performance data
        HistoricalPerformanceModel.objects.create(
            vendor=vendor,
            date=timezone.now(),  # Use timezone.now() for timezone-aware datetime
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate,
        )

        return {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfillment_rate': fulfillment_rate,
        }