from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="Pizza", price=10, inventory=100)
        Menu.objects.create(title="Burger", price=20, inventory=200)
        
    def test_getall(self):
        items = Menu.objects.all()
        serialized_data = MenuSerializer(items, many=True).data
        
        response = self.client.get('/restaurant/menu/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serialized_data)