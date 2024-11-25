from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'vehiculo/index.html')

def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})

@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})

