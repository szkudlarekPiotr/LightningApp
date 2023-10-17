from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from Lightning.Restaurants.models import Restaurant

# Create your models here.
class OrdersHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    total_price = models.FloatField()
    items = ArrayField(models.CharField(), default=[])
    order_date = models.DateTimeField(auto_now_add=True)