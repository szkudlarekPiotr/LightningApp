from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=500)
    cusine_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

class BusinessHours(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    day = models.IntegerField()
    open_time = models.IntegerField()
    close_time = models.IntegerField()
    