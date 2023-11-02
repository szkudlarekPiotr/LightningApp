from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

default_router = DefaultRouter()

default_router.register(r"cart", views.CartView)

urlpatterns = [
    path("", include(default_router.urls))
    #     path("", include(views.api_root)),
    #     path("cart/", views.UserCartsView.as_view()),
    #     path("<int:pk>/", views.CartView.as_view()),
]
