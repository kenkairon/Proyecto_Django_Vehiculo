# Proyecto_Django_Vehiculo
Educativo y de Aprendizaje Personal

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activar el entorno virtual](#Activar-el-entorno-virtual)
- [Instalar Django y Guardar dependencias](#Instalar-Django-y-Guardar-dependencias)
- [Pasos del Proyecto](#Pasos-del-Proyecto)



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