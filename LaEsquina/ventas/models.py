from django.db import models
from django.forms import model_to_dict

# Create your models here.
class usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ### Elecciones ara campo 'rol'
    class Rol(models.TextChoices):
        ADMINISTRADOR = 'Admin'
        BODEGUERO ='Bodeguero'
        CAJERO = 'Cajero'
    rol = models.CharField(
        max_length=30,
        choices=Rol.choices,
    )
    def __str__(self):
        return f"{self.nombre_usuario} ({self.rol})"

class proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombre_proveedor = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre_proveedor} ({self.rut})"

class producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    descripcion = models.TextField(max_length=500)
    precio_costo = models.FloatField()
    precio_venta = models.FloatField()
    stock_actual = models.IntegerField()
    stock_minimo = models.IntegerField()
    id_proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre_producto} (SKU: {self.sku})"
    
class venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    total_venta = models.FloatField()
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    def __str__(self):
        return f"Venta {self.id_venta} - Total: {self.total_venta}"
    
class detalle_venta(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_venta = models.ForeignKey(venta, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario_venta = models.FloatField()
    def __str__(self):
        return f"DetalleVenta {self.id_detalle_venta} - Producto: {self.id_producto.nombre_producto} - Cantidad: {self.cantidad} "
    
class empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=200)
    rut_empresa = models.CharField(max_length=12)
    direccion = models.CharField(max_length=300)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre_empresa} ({self.rut_empresa})"