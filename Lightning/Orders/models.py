from django.db import models
from django.contrib.auth.models import User
from Lightning.Restaurants.models import Restaurant

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    total_price = models.FloatField()
    items = models.CharField()
    order_date = models.DateTimeField(auto_now_add=True)