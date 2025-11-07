from django.contrib import admin
from .models import Cliente, Pedido, Empleado

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'email', 'telefono', 'fecha_registro')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'id_cliente', 'id_empleado', 'fecha_pedido', 'total', 'estado')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'nombre', 'apellido', 'puesto', 'fecha_ingreso')