# main/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from .models import Car, Order

class OrderViewTest(TestCase):
    def test_order_taxi_view(self):
        response = self.client.get(reverse('order_taxi'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_taxi.html')

    def test_order_taxi_post(self):
        car = Car.objects.create(car_class="Economy")
        data = {
            'pickup_location': 'A',
            'destination': 'B',
            'pickup_time': '2023-12-31T12:00:00',
            'car': car.id,
        }
        response = self.client.post(reverse('order_taxi'), data)
        self.assertEqual(response.status_code, 302)  # 302 is a redirect status code
        self.assertEqual(Order.objects.count(), 1)
