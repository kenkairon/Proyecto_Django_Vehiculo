from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_vehiculo, name='add_vehiculo'),
    path('list/', views.listar_vehiculos, name='listar_vehiculos'),
]
