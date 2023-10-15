from rest_framework import serializers
from .models import Restaurant, BusinessHours
from datetime import datetime


class RestaurantSerializer(serializers.ModelSerializer):
    opening_hour = serializers.SerializerMethodField()
    closing_hour = serializers.SerializerMethodField()
    today = datetime.now().isoweekday()

    class Meta:
        model = Restaurant
        fields = ["name","location", "cusine_type","opening_hour", "closing_hour", "is_active"]

    def get_opening_hour(self, obj):
        opening_hour = BusinessHours.objects.filter(restaurant=obj.id, day=self.today).values_list('open_time', flat=True)[0]
        return opening_hour
    
    def get_closing_hour(self, obj):
        closing_hour = BusinessHours.objects.filter(restaurant=obj.id, day=self.today).values_list('close_time', flat=True)[0]
        return closing_hour