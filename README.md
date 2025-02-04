# Proyecto_Django_Vehiculo
Educativo y de Aprendizaje Personal

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activar el entorno virtual](#Activar-el-entorno-virtual)
- [Instalar Django y Guardar dependencias](#Instalar-Django-y-Guardar-dependencias)
- [Pasos del Proyecto](#Pasos-del-Proyecto)
   - [Creación del SuperUsuario Y Configuraciones](#Creación-del-SuperUsuario-Y-Configuraciones)


## Requisitos

- Python 3.9 o superior
- Django 4.0 o superior
- Bootstrap 5

## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv proyecto_vehiculos_django

## Activar el entorno virtual

2. Activar el entorno virtual:
   ### Windows
   ```bash
   proyecto_vehiculos_django\Scripts\activate

## Instalar Django y Guardar dependencias

3. Intalación Django
   ```bash
   pip install Django==4.0.5 django-bootstrap-v5==1.0.11 django-crispy-forms==1.14.0 crispy-bootstrap5==0.6

4. Instalación dependencias
   ```bash
   pip freeze > requirements.txt

## Pasos del Proyecto

5. Crear el Proyecto
   ```bash
   django-admin startproject config

6. Ingresar al directorio del Proyecto config
   ```bash
   cd config

7. Crear la aplicación Vehículo
   ```bash
   python manage.py startapp vehiculo

8. Conectar el proyecto con la aplicación: Agregar 'vehiculo'  en la lista INSTALLED_APPS dentro del archivo config/settings.py:
   ```bash
   # Application definition
   INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'vehiculo',
      'bootstrap5',
   ]
9. Definir el vehiculo/models.py
   ```bash
   from django.db import models
   class Vehiculo(models.Model):      
      MARCA_CHOICES = [
         ('Fiat', 'Fiat'),
         ('Chevrolet', 'Chevrolet'),
         ('Ford', 'Ford'),
         ('Toyota', 'Toyota'),
      ]
      CATEGORIA_CHOICES = [
         ('Particular', 'Particular'),
         ('Transporte', 'Transporte'),
         ('Carga', 'Carga'),
      ]
      usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
      marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='Ford')
      modelo = models.CharField(max_length=100)
      serial_carroceria = models.CharField(max_length=50)
      serial_motor = models.CharField(max_length=50)
      categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Particular')
      precio = models.DecimalField(max_digits=10, decimal_places=2)
      fecha_creacion = models.DateTimeField(auto_now_add=True)
      fecha_modificacion = models.DateTimeField(auto_now=True)

      def __str__(self):
         return f"{self.marca} {self.modelo}"

10. Registrar el models en vehiculo/admin.py:

      ```bash
      from django.contrib import admin
      from .models import Vehiculo

      admin.site.register(Vehiculo)

11. colocamos los siguientes comandos
    
      ```bash
      python manage.py makemigrations
      python manage.py migrate

12. Creamos las vistas  vehiculos/views.py
      ```bash	
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

13. Creamos los templates\vehiculos\listar.html
      ```bash 
      {% extends 'base.html' %}

      {% block title %}Vehículos{% endblock %}

      {% block content %}
      {% if messages %}
      <div class="mb-3" id="message-container">
         {% for message in messages %}
         <div
            class="alert {% if message.tags == 'success' %} alert-success {%else%} alert-danger {%endif%} rounded-3 d-flex justify-content-between align-items-center">
            <span>{{ message }}</span>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
         </div>
         {% endfor %}
      </div>
      {% endif %}
      <div class="container mt-4">
         <h1 class="mb-4">Listado de Vehículos</h1>
         <div class="mt-1">
            <a class="btn btn-dark" href="{% url 'add_vehiculo' %}">Agregar Vehículos</a>
         </div>
         <hr>
         <div class="table-responsive">
            <table class="table table-striped border rounded-3 overflow-hidden">
                  <thead class="table-dark">
                     <tr>
                        <th scope="col">#</th>
                        <th scope="col">Marca</th>
                        <th scope="col">Modelo</th>
                        <th scope="col">Serial Carrocería</th>
                        <th scope="col">Serial Motor</th>
                        <th scope="col">Categoría</th>
                        <th scope="col">Precio</th>
                        <th scope="col">Condición de Precio</th>
                     </tr>
                  </thead>
                  <tbody>
                     {% for vehiculo in vehiculos %}
                     <tr>
                        <th scope="row">{{ forloop.counter }}</th>
                        <td>{{ vehiculo.marca }}</td>
                        <td>{{ vehiculo.modelo }}</td>
                        <td>{{ vehiculo.serial_carroceria }}</td>
                        <td>{{ vehiculo.serial_motor }}</td>
                        <td>{{ vehiculo.categoria }}</td>
                        <td>${{ vehiculo.precio }}</td>
                        <td>{{ vehiculo.condicion_precio }}</td>
                     </tr>
                     {% empty %}
                     <tr>
                        <td colspan="8" class="text-center">No hay vehículos disponibles</td>
                     </tr>
                     {% endfor %}
                  </tbody>
            </table>
         </div>
      </div>
      {% endblock %}

14. Creamos los templates\vehiculos\index.html
      ```bash
      {% extends 'base.html' %}
      <!-- Main Content -->
      <div class="container mt-5">
         <h1 class="text-center">Página Principal</h1>
         {% if user.is_authenticated %}
         <h2 class="text-center">Usuario autenticado</h2>
         <p class="text-center">Hello, {{ user.username }}!</p>
         {% block content %}
         <!-- Contenido específico de la página aquí -->
         <h1>Catálogo de Vehículos</h1>
         {% endblock %}
         {% else %}
         <h2 class="text-center text-danger">Acceso Restringido</h2>
         <p class="text-center">
            <a href="{% url 'login' %}" class="btn btn-primary">Iniciar Sesión</a>
         </p>
         {% endif %}
      </div>

15. Creamos los templates\vehiculos\add_vehiculo.html
      ```bash
      {% extends 'base.html' %}
      {% block content %}
      <div class="container mt-4">
         <h1 class="mb-4">Formulario</h1>
         <!-- Contenedor para el formulario -->
         <div class="card shadow-sm p-4 border rounded">
            <form method="post">
                  {% csrf_token %}
                  <div class="mb-3">
                     {{ form.as_p }}
                  </div>
                  <button type="submit" class="btn btn-primary">Enviar</button>
            </form>
         </div>
      </div>
      {% endblock %}
## Creación del SuperUsuario Y Configuraciones
16. Creamos un superusuario 

      ```bash
      python manage.py createsuperuser

17. Verificamos usuario y contraseña del superuser por motivos de aprendizaje le vamos a dar estos parametros pero que no son seguros
      ```bash
      admin
      admin@gmail.com
      admin1234
      y

18. Hacemos Correr en el Servidor nuestra Aplicación

      ```bash
      python manage.py runserver

19. Nos situamos en la pagina admin  http://127.0.0.1:8000/admin

      ```bash
      admin
      admin1234  

20. Para Probar la Aplicacion puede logearse o crear un usuario o probar directamente con las credenciales de administrador 
   ```bash
   http://127.0.0.1:8000/vehiculo/login/

21. Y si no tienes cuenta registrate 

   ```bash
   http://127.0.0.1:8000/vehiculo/registro/

22. Una vez registrado o logeado , puedes agregar vehiculos
   ```bash
   http://127.0.0.1:8000/vehiculo/add/

23. y listar vehiculos
   ```bash
   http://127.0.0.1:8000/vehiculo/list/