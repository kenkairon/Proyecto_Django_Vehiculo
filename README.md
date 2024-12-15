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
9. Configuración de los archivso static 
   ```bash
   import os
   STATIC_URL = 'static/'
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

10. Definir el vehiculo/models.py

   ```bash
      from django.db import models
      from django.contrib.auth.models import Permission
      from django.contrib.contenttypes.models import ContentType
      from django.contrib.auth.models import User
      from django.db.models.signals import post_save
      from django.dispatch import receiver


      @receiver(post_save, sender=User)
      def asignar_permiso_visualizar_catalogo(sender, instance, created, **kwargs):
         if created:  # Solo al registrar un nuevo usuario
            content_type = ContentType.objects.get(app_label='vehiculo', model='vehiculo')
            permiso = Permission.objects.get(content_type=content_type, codename='visualizar_catalogo')
            instance.user_permissions.add(permiso)

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
         
         
         class Meta:
            permissions = [
                  ('visualizar_catalogo', 'Puede visualizar el catálogo de vehículos'),
      ]

11. creamos en vehiculo/forms.py 

   ```bash
   from django import forms
   from .models import Vehiculo

   class VehiculoForm(forms.ModelForm):
      class Meta:
         model = Vehiculo
         fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']

12. Creamos vehiculo/formulario.py para razones de registro cin RegisterForm

   ```bash
   from django import forms
   from django.contrib.auth.models import User

   class RegisterForm(forms.Form):
      username = forms.CharField(
         required=True,
         min_length=4, 
         max_length=50,
         widget=forms.TextInput(attrs={
               'class': 'form-control form-control-lg',  # Clase personalizada para field grandes
               'id': 'username',
               'placeholder': 'Username'
         })
      )
      email = forms.EmailField(
         required=True,
         widget=forms.EmailInput(attrs={
               'class': 'form-control form-control-lg',  # Clase personalizada
               'id': 'email',
               'placeholder': 'example@gmail.com'
         })
      )
      password = forms.CharField(
         required=True,
         widget=forms.PasswordInput(attrs={
               'class': 'form-control form-control-lg',  # Clase personalizada
               'id': 'password',
               'placeholder': 'Password'
         })
      )
      
      def clean_username(self):
         username = self.cleaned_data.get('username')

         if User.objects.filter(username=username).exists():
               raise forms.ValidationError('El username ya se encuentra en uso')

         return username

      def clean_email(self):
         email = self.cleaned_data.get('email')

         if User.objects.filter(email=email).exists():
               raise forms.ValidationError('El email ya se encuentra en uso')

         return email

13. templates/user/login.html
14. templates/user/register.html
15. templates/vehculo/add_vehiculo.html.
16. templates/vehiculo/index.html
17. templates/vehiculo/listar.html
18. Registrar el models en vehiculo/admin.py:
      ```bash
      from django.contrib import admin
      from .models import Vehiculo

      admin.site.register(Vehiculo)

19. colocamos los siguientes comandos
    
      ```bash
      python manage.py makemigrations
      python manage.py migrate


## Creación del SuperUsuario Y Configuraciones
20. Creamos un superusuario 

      ```bash
      python manage.py createsuperuser

21. Verificamos usuario y contraseña del superuser por motivos de aprendizaje le vamos a dar estos parametros pero que no son seguros
      ```bash
      admin
      admin@gmail.com
      admin1234
      y

22. Hacemos Correr en el Servidor nuestra Aplicación

      ```bash
      python manage.py runserver

23. Nos situamos en la pagina admin  http://127.0.0.1:8000/admin

      ```bash
      admin
      admin1234  

24. Para Probar la Aplicacion puede logearse o crear un usuario o probar directamente con las credenciales de administrador 

      ```bash
         admin
         admin1234 