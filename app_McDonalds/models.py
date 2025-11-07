from django.db import models

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_registro = models.DateField(auto_now_add=True)
    fecha_nacimiento = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: PEDIDO
# ==========================================
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    id_empleado = models.IntegerField()  # ID de empleado, relacionado con la tabla Empleados
    fecha_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=30, choices=[('Pendiente', 'Pendiente'), ('Enviado', 'Enviado'), ('Entregado', 'Entregado')])
    direccion = models.TextField()
    forma_pago = models.CharField(max_length=20, choices=[('Efectivo', 'Efectivo'), ('Tarjeta', 'Tarjeta')])
    
    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.id_cliente.nombre} {self.id_cliente.apellido}"

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    fecha_ingreso = models.DateField(auto_now_add=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(max_length=15)
    horario = models.CharField(max_length=20)  # Horario de trabajo (Ejemplo: Mañana, Tarde)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.puesto}"