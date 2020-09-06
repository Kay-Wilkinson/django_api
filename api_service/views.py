from rest_framework import viewsets

from .serializers import FoodMenuItemSerializer
from .models import FoodMenuItems


class FoodMenuItemViewSet(viewsets.ModelViewSet):
    # Return all FoodItem objects by price in descending order
    queryset = FoodMenuItems.objects.all().order_by('-food_item_price')
    serializer_class = FoodMenuItemSerializer