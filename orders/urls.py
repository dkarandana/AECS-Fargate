from django.contrib import admin
from django.urls import path, include

from .views import (
    PlaceOrderView, OrderListView,
    OrderDetailView
)

app_name = "orders"

urlpatterns = [
    path('detail/<int:pk>/', OrderDetailView.as_view(), name="order_detail"),
    path('place-order/', PlaceOrderView.as_view(), name="place_order"),
    path('list/', OrderListView.as_view(), name="order_list"),
]
