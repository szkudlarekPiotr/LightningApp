from django.shortcuts import render, redirect
from .models import Cart
from .serializers import CartSerializer
from rest_framework import permissions, viewsets
from RestaurantMenu.models import MenuItem

#TODO : check if request data isn't empty

# Create your views here.
class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user).all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        cart_objects = self.get_queryset()
        request_item = MenuItem.objects.get(id=self.request.data["item"])
        for cart in cart_objects:
            if request_item == cart.item:
                cart.decrease_quantity()
                return redirect('/cart')
        print(Cart.objects.create(item=request_item, quantity=self.request.GET.get("quantity", 1), owner=self.request.user))
        return redirect('/cart')

