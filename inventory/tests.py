# inventory/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Item

class ItemModelTest(TestCase):
    def test_create_item(self):
        item = Item.objects.create(name="Test Item", price=10.0, quantity=5)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.price, 10.0)
        self.assertEqual(item.quantity, 5)

class ItemViewTest(TestCase):
    def test_item_list_view(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, 200)
