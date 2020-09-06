from django.db import models


class FoodMenuItems(models.Model):
    food_item_name = models.CharField(max_length=60)
    food_item_description = models.CharField(max_length=120)
    food_item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_item_details(self):
        return self.food_item_name + " is €" + str(self.food_item_price)

    def __repr__(self):
        return self.food_item_name + ' added to model.'