from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username', 'email', 
            'first_name', 'last_name',
            'acc_status', 'is_superuser', 'is_staff',
            'register_date', 'last_update_date'
        ]