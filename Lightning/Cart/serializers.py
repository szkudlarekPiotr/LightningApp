from rest_framework import serializers
from .models import Cart


class ListCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "date_created"]


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["item", "quantity"]
