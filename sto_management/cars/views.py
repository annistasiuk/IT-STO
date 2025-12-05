from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CarForm
from .models import Car
from django.contrib import messages

def add_car_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            new_car = form.save()
            messages.success(request, f'Авто "{new_car.make} {new_car.model_name}" додано! Тепер створіть заявку на ремонт.')

            return redirect(f"{reverse('add_repair')}?car_id={new_car.id}")
    else:
        form = CarForm()

    return render(request, 'cars/add_car.html', {'form': form})


def car_list_view(request):
    cars = Car.objects.all().order_by('-id')
    return render(request, 'cars/car_list.html', {'cars': cars})


def delete_car_view(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        car.delete()
        messages.success(request, f'Авто "{car.make} {car.model_name}" успішно видалено.')
        return redirect('car_list')

    return render(request, 'cars/car_confirm_delete.html', {'car': car})