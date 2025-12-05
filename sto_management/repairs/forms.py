from django import forms
from .models import Repair

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['car', 'description', 'status']
        labels = {
            'car': 'Автомобіль',
            'description': 'Запчастини',
            'status': 'Статус ремонту',
        }