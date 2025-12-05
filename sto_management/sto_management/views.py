from django.shortcuts import render
from cars.models import Car
from repairs.models import Repair
from django.db.models import Sum


def home_view(request):
    """
    Головна сторінка: Статистика та Останні авто.
    """

    # 1. Загальна кількість авто (потрібно для картки "БАЗА АВТО")
    total_cars = Car.objects.count()

    # 2. Статистика ремонтів
    try:
        # У новому шаблоні home.html змінні називаються 'in_progress' та 'completed'
        in_progress = Repair.objects.filter(status='in_progress').count()
        completed = Repair.objects.filter(status='completed').count()

        # Ваша логіка розрахунку доходу
        total_income = completed * 1500
    except Exception:
        in_progress = 0
        completed = 0
        total_income = 0

    # 3. Останні надходження (для таблиці)
    latest_cars = Car.objects.all().order_by('-created_at')[:5]

    context = {
        'total_cars': total_cars,  # Обов'язково для картки авто
        'in_progress': in_progress,  # Обов'язково для статистики (червона картка)
        'completed': completed,  # Обов'язково для статистики
        'total_income': total_income,  # Дохід (можна вивести в шаблон пізніше)
        'latest_cars': latest_cars,  # Список для таблиці внизу
    }

    return render(request, 'home.html', context)