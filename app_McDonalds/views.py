from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from django.utils import timezone

# Inicio
def inicio_mcdonalds(request):
    # resumen simple: cantidad de clientes
    total_clientes = Cliente.objects.count()
    return render(request, 'inicio.html', {'total_clientes': total_clientes})

# Agregar cliente (muestra formulario y procesa POST)
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellido = request.POST.get('apellido', '')
        email = request.POST.get('email', '')
        telefono = request.POST.get('telefono', '')
        direccion = request.POST.get('direccion', '')
        fecha_nacimiento = request.POST.get('fecha_nacimiento', None)

        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion,
            fecha_nacimiento=fecha_nacimiento
        )
        cliente.save()
        return redirect('app_McDonalds:ver_clientes')

    return render(request, 'cliente/agregar_cliente.html')

# Ver clientes (lista)
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('-fecha_registro')
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

# Mostrar formulario de actualizar (cargar datos)
def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

# Procesar actualización
def realizar_actualizacion_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre', cliente.nombre)
        cliente.apellido = request.POST.get('apellido', cliente.apellido)
        cliente.email = request.POST.get('email', cliente.email)
        cliente.telefono = request.POST.get('telefono', cliente.telefono)
        cliente.direccion = request.POST.get('direccion', cliente.direccion)
        fecha_nac = request.POST.get('fecha_nacimiento', None)
        if fecha_nac:
            cliente.fecha_nacimiento = fecha_nac
        cliente.save()
        return redirect('app_McDonalds:ver_clientes')
    return redirect('app_McDonalds:actualizar_cliente', id_cliente=id_cliente)

# Borrar cliente (confirmación y eliminación)
def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('app_McDonalds:ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})