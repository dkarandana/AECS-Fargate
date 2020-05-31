from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    tracking_code = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id", "total_amount", "customer_name", "customer_email",
            "status", "create_date", "last_update_date", "tracking_code"
        ]

    def get_tracking_code(self, instance):
        
        try:
            delivery = instance.delivery   

        except Exception as err:
            return None
            
        else:
            return delivery.id


    