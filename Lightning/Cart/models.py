from django.db import models
from django.contrib.auth.models import User
from RestaurantMenu.models import MenuItem
# Create your models here.

class Cart(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def increase_quantity(self):
        self.quantity +=1
        self.save()
    
    def decrease_quantity(self):
        self.quantity -=1
        if self.quantity <= 0:
            print('zero mam')
            self.delete()
        else:
            self.save()