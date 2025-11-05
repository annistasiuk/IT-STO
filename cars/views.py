from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CarForm
from django.contrib import messages

def add_car_view(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Автомобіль успішно додано!')
            return redirect('car_list')
    else:
        form = CarForm()

    return render(request, 'cars/add_car.html', {'form': form})

def car_list_view(request):
    return HttpResponse("Це сторінка списку авто")