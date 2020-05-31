from random import randrange

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView
)
from faker import Faker

from .models import Order
from delivery.models import Delivery
from .serializers import OrderSerializer

class PlaceOrderView(CreateAPIView):
    
    fake = Faker()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):

        order_data = {
            "total_amount": randrange(1000, 10000),
            "customer_name": self.fake.name(),
            "customer_email": self.fake.email(),
        }

        serializer = self.serializer_class(data=order_data)
        
        # if valid create order object and delivery object
        if serializer.is_valid():

            order = serializer.save()
            order_serializer = self.serializer_class(instance=order)
            self._create_delivery(order=order)

            return Response(order_serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def _create_delivery(self, order):
        
        delivery = Delivery(order=order)
        delivery.save()

class OrderListView(ListAPIView):

    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("-id")

class OrderDetailView(RetrieveAPIView):

    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


