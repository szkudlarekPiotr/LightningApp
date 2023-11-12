from django.shortcuts import redirect
from django.urls import reverse
from .models import Cart
from .serializers import CartSerializer
from rest_framework import permissions, viewsets, mixins, generics, status
from rest_framework.response import Response
from rest_framework.serializers import ValidationError


class UserCartsView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user).all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user).all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response(
                data={"message": f"{e.detail['products'][0]}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            user_carts = Cart.objects.get(owner=request.user)
        except Cart.DoesNotExist:
            return super(CartView, self).create(request, *args, **kwargs)
        else:
            return redirect(f"{user_carts.id}/")

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)
