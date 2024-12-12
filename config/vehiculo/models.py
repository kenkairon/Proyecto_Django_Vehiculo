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

 
   