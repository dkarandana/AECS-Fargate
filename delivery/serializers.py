from rest_framework import serializers

from .models import Delivery

class DeliverySerializer(serializers.ModelSerializer):

    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Delivery
        fields = "__all__"