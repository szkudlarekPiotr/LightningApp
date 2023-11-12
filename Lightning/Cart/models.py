from django.db import models
from django.contrib.auth.models import User
import json


class Cart(models.Model):
    products = models.JSONField(null=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    # def increase_quantity(self):
    #     self.quantity += 1
    #     self.save()

    # def decrease_quantity(self):
    #     self.quantity -= 1
    #     if self.quantity <= 0:
    #         self.delete()
    #     else:
    #         self.save()
    def __str__(self):
        return json.dumps(self.products)
