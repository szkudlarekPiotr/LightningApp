from django.shortcuts import render
from rest_framework import mixins, generics
from .models import MenuItem
from .serializers import MenuSerializer

class ListMenuItems(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer

    def get(self, request, *args, **kwargs,):
        print(self.kwargs["id"])
        self.queryset = MenuItem.objects.filter(restaurant=self.kwargs['id'])
        return self.list(request, *args, **kwargs)