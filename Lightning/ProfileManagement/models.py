from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=500)