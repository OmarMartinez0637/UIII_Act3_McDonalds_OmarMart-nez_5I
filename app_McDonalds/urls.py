from django.urls import path
from . import views

app_name = 'app_McDonalds'

urlpatterns = [
    path('', views.inicio_mcdonalds, name='inicio'),
    # Clientes
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_clientes, name='ver_clientes'),
    path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/actualizar/realizar/<int:id_cliente>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id_cliente>/', views.borrar_cliente, name='borrar_cliente'),
]