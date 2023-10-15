from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.ListMenuItems.as_view(), name="menu"),
]
