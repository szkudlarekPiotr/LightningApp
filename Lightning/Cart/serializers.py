from rest_framework import serializers
from rest_framework.validators import ValidationError
from RestaurantMenu.models import MenuItem
from .models import Cart


class CartProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    extra_kwargs = {"id": {"required": False, "read_only": False}}

    def to_representation(self, instance):
        return super().to_representation(instance)


class CartSerializer(serializers.ModelSerializer):
    products = CartProductsSerializer(many=True)

    class Meta:
        model = Cart
        fields = ["products", "date_created"]

    def to_representation(self, instance):
        menu_items = instance.products
        products_id = [item["id"] for item in menu_items]
        menu_items = MenuItem.objects.in_bulk(products_id)
        menu_items = [
            {"id": key, "name": value.name, "price": value.price}
            for key, value in menu_items.items()
        ]
        return {
            "id": instance.id,
            "date_created": instance.date_created,
            "products": menu_items,
        }

    def validate_products(self, data):
        items = [item["id"] for item in data]
        db_items = MenuItem.objects.in_bulk(items)
        if len(items) != len(db_items):
            for item in items:
                if item not in db_items:
                    raise ValidationError(f"Item of id {item} does not exist.")
        return data
