# main/views.py
from django.shortcuts import render, redirect
from .models import Order, Car


def order_taxi(request):
    if request.method == 'POST':
        # Обработка данных формы и создание заказа
        pickup_location = request.POST.get('pickup_location')
        destination = request.POST.get('destination')
        pickup_time = request.POST.get('pickup_time')
        car_id = request.POST.get('car')

        car = Car.objects.get(id=car_id)
        order = Order.objects.create(
            pickup_location=pickup_location,
            destination=destination,
            pickup_time=pickup_time,
            car=car
        )

        # Дополнительная логика обработки заказа

        return redirect('order_confirmation')

    # Получение списка автомобилей для формы
    cars = Car.objects.all()
    return render(request, 'order_taxi.html', {'cars': cars})


def order_confirmation(request):
    # Получите данные заказа, например, из последнего созданного заказа
    order = Order.objects.latest('id')
    return render(request, 'order_confirmation.html', {'order': order})