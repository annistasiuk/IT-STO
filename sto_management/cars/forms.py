from django import forms
from .models import Car
import datetime


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'make', 'model_name',
            'vin', 'owner_name',
            'year', 'color',
            'transmission', 'fuel_type',
            'description',
            'main_image'
        ]

        widgets = {
            'make': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наприклад: BMW, Audi, Toyota'
            }),
            'model_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наприклад: X5, Passat'
            }),
            'vin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть 17 символів VIN',
                'maxlength': '17',
                'style': 'text-transform: uppercase;'
            }),
            'owner_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ПІБ власника'
            }),
            # -----------------------------------
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1900,
                'max': datetime.date.today().year + 1
            }),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-select'}),
            'fuel_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Детальний опис автомобіля...'
            }),
            'main_image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        current_year = datetime.date.today().year

        if year and year > current_year + 1:
            raise forms.ValidationError(f"Рік випуску не може бути більшим за {current_year + 1}.")

        return year

    def clean_vin(self):
        vin = self.cleaned_data.get('vin')
        if vin:
            return vin.upper()
        return vin