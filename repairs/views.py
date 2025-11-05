from django.shortcuts import render
from .models import Repair

def repair_list_view(request):
    status_filter = request.GET.get('status', '')

    repairs = Repair.objects.select_related('car').all()

    if status_filter:
        repairs = repairs.filter(status=status_filter)

    status_choices = Repair.STATUS_CHOICES

    context = {
        'repairs': repairs,
        'status_choices': status_choices,
        'current_filter': status_filter
    }
    return render(request, 'repairs/repair_list.html', context)