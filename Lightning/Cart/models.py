from django.db import models
from django.contrib.auth.models import User
from RestaurantMenu.models import MenuItem

# TODO: Change item field to products - Json field containing product id, name and quantity


class Cart(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    owner = models.OneToOneField(User, related_name="User", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def increase_quantity(self):
        self.quantity += 1
        self.save()

    def decrease_quantity(self):
        self.quantity -= 1
        if self.quantity <= 0:
            self.delete()
        else:
            self.save()
