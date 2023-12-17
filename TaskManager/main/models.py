# main/models.py
from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    # Другие поля для описания автомобиля
    CLASS_CHOICES = [
        ('Economy', 'Economy'),
        ('Standard', 'Standard'),
        ('Luxury', 'Luxury'),
    ]
    car_class = models.CharField(max_length=20, choices=CLASS_CHOICES)

class Order(models.Model):
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    pickup_time = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    # Другие поля для заказа

class Review(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    # Другие поля для отзыва
