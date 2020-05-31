from django.db import models

from orders.models import Order

class Delivery(models.Model):
    
    DRIVER_ACCEPTED = "1"
    DRIVER_AT_PICKUP_LOCATION = "2"
    ITEM_PICKED = "3"
    REACHED_DESTINATION = "4"
    UNLOADED = "5"
    COMPLEATED = "6"
    BOOKING_CANCELD = "0"

    STATUS_CHOICES = [
        (DRIVER_ACCEPTED, 'DRIVER ACCEPTED'),
        (DRIVER_AT_PICKUP_LOCATION, 'DRIVER AT PICKUP LOCATION'),
        (ITEM_PICKED, 'ITEM PICKED && ON GOING'),
        (REACHED_DESTINATION, 'REACHED DESTINATION'),
        (UNLOADED, 'UNLOADED'),
        (COMPLEATED, 'COMPLETED'),
        (BOOKING_CANCELD, "BOOKING_WAS_CANCELD")
    ]

    order = models.OneToOneField(to=Order, on_delete=models.CASCADE)

    status = models.CharField(
        verbose_name="Status", 
        choices=STATUS_CHOICES, 
        max_length=50,
        default=DRIVER_ACCEPTED
    )
    