import json
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework import status
from Restaurants.models import Restaurant
from RestaurantMenu.models import MenuItem
from .models import Cart


class AddItemsToCart(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create_user(
            id=12372, username="test", password="test"
        )
        self.test_user.save()
        self.client.force_login(self.test_user)
        self.path = "http://127.0.0.1:8000/cart/"
        self.test_restaurant = Restaurant.objects.create(
            name="name", location="location", cusine_type="type", is_active=True
        )
        self.test_item1 = MenuItem.objects.create(
            name="item1",
            description="desc",
            picture="pic",
            is_available=True,
            dish_type="type",
            price=100,
            restaurant_id=self.test_restaurant.id,
        )

    def test_GetOwnCart(self):
        get_request = self.client.get(self.path)
        self.assertEqual(get_request.status_code, status.HTTP_200_OK)

    def test_CantAddNotExistingItems(self):
        data = {"products": [{"id": self.test_item1.id}, {"id": 99999}]}
        json_data = json.dumps(data)
        post_request1 = self.client.post(
            self.path, data=json_data, content_type="application/json"
        )
        self.assertEqual(post_request1.status_code, status.HTTP_400_BAD_REQUEST)

    def test_CanAddExistingItems(self):
        data = {"products": [{"id": self.test_item1.id}]}
        json_data = json.dumps(data)
        post_request1 = self.client.post(
            self.path, data=json_data, content_type="application/json"
        )
        self.assertEqual(post_request1.status_code, status.HTTP_201_CREATED)

    def test_RedirectionToOwnCart(self):
        self.test_cart = Cart.objects.create(
            owner=self.test_user, products=[{"id": self.test_item1.id}]
        )
        data = {"products": [{"id": self.test_item1.id}]}
        json_data = json.dumps(data)
        post_request1 = self.client.post(
            self.path, data=json_data, content_type="application/json"
        )
        self.assertEqual(post_request1.status_code, status.HTTP_302_FOUND)
