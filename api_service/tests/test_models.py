from django.test import TestCase

from ..models import FoodMenuItems


class FoodMenuItemsModelTest(TestCase):
    def setUp(self):
        FoodMenuItems.objects.create(
            food_item_name='Test Food Name',
            food_item_description='Test Food Description',
            food_item_price='5.00',
        )

    def test_food_item_detail(self):
        test_expected_data_returned = FoodMenuItems.objects.get(food_item_name='Test Food Name')
        self.assertEqual(
            test_expected_data_returned.get_item_details(), 'Test Food Name is €5.00'
        )

    def test_decimal_price(self):
        price_datatype = FoodMenuItems.objects.get(food_item_name='Test Food Name')
        self.assertNotEqual(
            # Test that the DecimalField that
            price_datatype.get_item_details(), 'Test Food Name is €5'
        )