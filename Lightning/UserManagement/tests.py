from ast import Delete
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.reverse import reverse


class CanManageProfiles(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_user = User.objects.create_user(username="test", password="test")
        self.test_user.save()
        self.other_user = User.objects.create_user(username="test2", password="test2")
        self.other_user.save()
        self.client.login(username="test", password="test")
        self.own_profile = (
            f"http://127.0.0.1:8000/user/{self.test_user.id}/",
            {"username": "test"},
        )
        self.other_profile = (
            f"http://127.0.0.1:8000/user/{self.other_user.id}/",
            {"username": "test"},
        )

    def tearDown(self):
        self.test_user.delete()
        self.other_user.delete()

    def test_CanManageOwnProfile(self):
        get = self.client.get(self.own_profile[0])
        head = self.client.head(self.own_profile[0])
        patch = self.client.patch(*self.own_profile)
        put = self.client.put(*self.own_profile)
        delete = self.client.delete(self.own_profile[0])
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(head.status_code, status.HTTP_200_OK)
        self.assertEqual(patch.status_code, status.HTTP_200_OK)
        self.assertEqual(put.status_code, status.HTTP_200_OK)
        self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_CanViewOtherProfiles(self):
        get = self.client.get(self.other_profile[0])
        head = self.client.head(self.other_profile[0])
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(head.status_code, status.HTTP_200_OK)

    def test_CanManageOtherProfiles(self):
        patch = self.client.patch(*self.other_profile)
        put = self.client.put(*self.other_profile)
        delete = self.client.delete(self.other_profile[0])
        self.assertEqual(patch.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(put.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(delete.status_code, status.HTTP_403_FORBIDDEN)
