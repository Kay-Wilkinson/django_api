import json

from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/food-menu-items', json.dumps({
    "food_item_name": "Snacks",
    "food_item_description": "Small bites",
    "food_item_price": "5.00"
}), content_type='application/json')