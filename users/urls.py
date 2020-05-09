from django.contrib import admin
from django.urls import path, include

from .views import UserProfileView

app_name = "users"

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name="view_profile"),
]
