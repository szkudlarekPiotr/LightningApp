from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

default_router = DefaultRouter()

default_router.register(r"cart", views.CartView)

urlpatterns = [
    path("", include(default_router.urls)),
]
