from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin,
    UserManager
)

class User(PermissionsMixin, AbstractBaseUser):

    username = models.CharField(
        verbose_name="Username",
        unique=True, max_length=255,
    )

    email = models.EmailField(
        verbose_name='Email',
        unique=True,
        max_length=255
    )

    acc_status = models.BooleanField(
        verbose_name="Account Status",
        default=True,
    )

    first_name = models.CharField(verbose_name="First Name", null=True, blank=True, max_length=255)

    last_name = models.CharField(verbose_name="Last Name", null=True, blank=True, max_length=255)

    is_superuser = models.BooleanField(verbose_name='Super User', default=False)
    
    is_staff = models.BooleanField(verbose_name='Staff User', default=False)

    register_date = models.DateTimeField(verbose_name="Register Date", auto_now_add=True)

    last_update_date = models.DateTimeField(verbose_name="Last Edited Date", auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def is_active(self):
        return self.acc_status
    
 