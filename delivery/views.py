from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .models import Delivery
from orders.models import Order
from .serializers import DeliverySerializer

class DeliveryStatusView(generics.RetrieveAPIView):
    
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

class CancelDeliveryView(generics.RetrieveAPIView):
    
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer

    def post(self, reqeust, *args, **kwargs):
        
        delivery_object = self.get_object()
        delivery_object.status = Delivery.BOOKING_CANCELD
        delivery_object.save()

        order = delivery_object.order
        order.status = Order.STATUS_CANCELD
        order.save()

        serializer = self.serializer_class(instance=delivery_object)
        return Response(serializer.data)

