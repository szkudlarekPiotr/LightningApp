from django.db.utils import IntegrityError
from django.shortcuts import redirect
from .models import Cart
from .serializers import CartItemsSerializer, ListCartSerializer
from rest_framework import permissions, viewsets, mixins, generics, status
from rest_framework.response import Response


# TODO : CZY UZYC GENERIC VIEWSET, CZY UZYC MIXINOW I ROBIC RECZNIE URL CZY MODELVIEWSET SPROBOWAC I METHOD CLASSES
# TODO: http_method_names = ['get', 'post', 'head']


class UserCartsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = ListCartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user).all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartItemsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user).all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError as e:
            user_cart = Cart.objects.get(owner=self.request.user.id)
            return redirect(
                f"{user_cart.id}/"
            )  # redirect user to own cart in case it already exists
        return self.create(request, *args, **kwargs)
