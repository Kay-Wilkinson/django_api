from rest_framework.test import APIRequestFactory, APITestCase

from ..views import FoodMenuItemViewSet


class GetRequestFoodItemsTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FoodMenuItemViewSet.as_view({'get': 'list'})
        self.uri = '/food-menu-items/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code,
                         200,
                         f'Expected response code: 200 OK. Received {response.status_code} instead')
