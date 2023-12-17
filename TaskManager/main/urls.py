from django.urls import path
from .views import order_taxi, order_confirmation

urlpatterns = [
    path('order/', order_taxi, name='order_taxi'),
    path('order/confirmation/', order_confirmation, name='order_confirmation'),
    # Другие маршруты
]
