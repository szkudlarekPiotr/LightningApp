from django.db import models
from Restaurants.models import Restaurant

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    picture= models.ImageField()
    is_available = models.BooleanField(default=True)
    dish_type = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.FloatField()
    