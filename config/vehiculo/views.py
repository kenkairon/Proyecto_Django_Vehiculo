from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .formulario import RegisterForm
from django.contrib.messages.storage.session import SessionStorage


def index(request):
    return render(request, 'vehiculo/index.html')


def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)  # No guardar aún en la base de datos
            vehiculo.usuario = request.user  # Asignar el usuario autenticado
            vehiculo.save()  # Ahora guardar en la base de datos
            messages.success(request, 'Vehículo agregado exitosamente.')
            return redirect('listar_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})


@login_required
@permission_required('vehiculo.visualizar_catalogo', raise_exception=True)
def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.filter(usuario=request.user)  # Filtrar por usuario
    for vehiculo in vehiculos:
        if vehiculo.precio <= 10000:
            vehiculo.condicion_precio = 'Bajo'
        elif 10000 < vehiculo.precio <= 30000:
            vehiculo.condicion_precio = 'Medio'
        else:
            vehiculo.condicion_precio = 'Alto'
    return render(request, 'vehiculo/listar.html', {'vehiculos': vehiculos})


def login_view(request):
    # Consumir y descartar los mensajes existentes
    list(messages.get_messages(request))
    
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Autenticar usuario
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')  # Cambia según la ruta de tu vista principal
        else:
            messages.error(request, 'Usuario o Contraseña no válidos')
    
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            #messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')
    return render(request, 'users/register.html', {'form': form})
