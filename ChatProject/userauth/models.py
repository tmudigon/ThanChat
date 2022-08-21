from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    address = models.CharField(max_length=500, null=True)
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name', 'email']
    USERNAME_FIELD = 'username'
