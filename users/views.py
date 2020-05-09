from django.shortcuts import render

from rest_framework import views, response, status
from rest_framework.response import Response

from .serializers import UserSerializer

class UserProfileView(views.APIView):

    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        
        user = request.user

        serializer = self.serializer_class(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
