from django.shortcuts import render, redirect, get_object_or_404
from .models import Repair
from .forms import RepairForm
from django.contrib import messages


def edit_repair_view(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)

    if request.method == 'POST':
        form = RepairForm(request.POST, instance=repair)
        if form.is_valid():
            form.save()
            messages.success(request, 'Зміни успішно збережено!')
            return redirect('repair_list')
    else:
        form = RepairForm(instance=repair)

    return render(request, 'repairs/edit_repair.html', {'form': form, 'repair': repair})


def repair_list_view(request):
    status_filter = request.GET.get('status', '')
    repairs = Repair.objects.select_related('car').all().order_by('-start_date')

    if status_filter:
        repairs = repairs.filter(status=status_filter)

    status_choices = Repair.STATUS_CHOICES

    context = {
        'repairs': repairs,
        'status_choices': status_choices,
        'current_filter': status_filter
    }
    return render(request, 'repairs/repair_list.html', context)


def add_repair_view(request):
    initial_data = {}
    car_id = request.GET.get('car_id')

    if car_id:
        initial_data['car'] = car_id

    if request.method == 'POST':
        form = RepairForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявку на ремонт успішно створено!')
            return redirect('repair_list')
    else:
        form = RepairForm(initial=initial_data)

    return render(request, 'repairs/add_repair.html', {'form': form})