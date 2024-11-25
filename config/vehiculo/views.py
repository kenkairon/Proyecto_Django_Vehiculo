from django.shortcuts import render, redirect
from .forms import VehiculoForm

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
