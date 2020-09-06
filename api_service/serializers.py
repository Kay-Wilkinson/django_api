from rest_framework import serializers

from .models import FoodMenuItems


class FoodMenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FoodMenuItems
        fields = ('food_item_name', 'food_item_description', 'food_item_price')