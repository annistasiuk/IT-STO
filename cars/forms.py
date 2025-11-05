from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {
            'make': 'Марка',
            'model': 'Модель',
            'year': 'Рік випуску',
            'vin': 'VIN-код',
            'owner_name': "Ім'я власника",
            'owner_phone': 'Телефон власника',
        }

    def clean_vin(self):
        vin = self.cleaned_data.get('vin')
        if len(vin) != 17:
            raise forms.ValidationError("VIN-код повинен складатися з 17 символів.")
        return vin

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 1980 or year > 2025:
            raise forms.ValidationError("Вкажіть коректний рік випуску.")
        return year

