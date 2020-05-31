from django.contrib import admin
from django.urls import path, include

from .views import DeliveryStatusView, CancelDeliveryView

app_name = "delivery"

urlpatterns = [
    path('status/<int:pk>/', DeliveryStatusView.as_view(), name="get_status"),
    path('cancel/<int:pk>/', CancelDeliveryView.as_view(), name="cancel_delivery")
]
