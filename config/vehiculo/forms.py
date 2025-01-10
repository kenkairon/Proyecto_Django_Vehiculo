from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'marca': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la marca del vehículo'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el modelo del vehículo'
            }),
            'serial_carroceria': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el serial de la carrocería'
            }),
            'serial_motor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el serial del motor'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio del vehículo',
                'min': '0',
                'step': '0.01'
            }),
        }
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'serial_carroceria': 'Serial de Carrocería',
            'serial_motor': 'Serial del Motor',
            'categoria': 'Categoría',
            'precio': 'Precio',
        }
