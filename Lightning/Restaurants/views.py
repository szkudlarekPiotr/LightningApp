from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import mixins, generics
from .serializers import RestaurantSerializer
from .models import Restaurant


class ListRestaurant(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)