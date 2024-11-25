# Proyecto_Django_Vehiculo
Educativo y de Aprendizaje Personal

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activar el entorno virtual](#Activar-el-entorno-virtual)
- [Instalar Django y Guardar dependencias](#Instalar-Django-y-Guardar-dependencias)
- [Pasos del Proyecto](#Pasos-del-Proyecto)
   -[Creación del SuperUsuario Y Configuraciones](#Creación-del-SuperUsuario-Y-Configuraciones)


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


## Creación del SuperUsuario Y Configuraciones
12. Creamos un superusuario 

      ```bash
      python manage.py createsuperuser

13. Verificamos usuario y contraseña del superuser por motivos de aprendizaje le vamos a dar estos parametros pero que no son seguros
      ```bash
      admin
      admin@gmail.com
      admin1234
      y

15. Hacemos Correr en el Servidor nuestra Aplicación

      ```bash
      python manage.py runserver

16. Nos situamos en la pagina admin  http://127.0.0.1:8000/admin

      ```bash
      admin
      admin1234    