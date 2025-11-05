from django.contrib import admin
from ventas.models import proveedor, producto, empresa, usuario
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'rut', 'nombre_proveedor', 'contacto')
    search_fields = ('nombre_proveedor', 'rut')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(proveedor, ProveedorAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre_usuario', 'password', 'rol')
    search_fields = ('nombre_usuario', 'rol')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(usuario, UsuarioAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'sku', 'nombre_producto', 'precio_venta', 'stock_actual', 'imagen', 'id_proveedor')
    search_fields = ('nombre_producto', 'sku')
    list_filter = ('id_proveedor',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(producto, ProductoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('id_empresa', 'nombre_empresa', 'rut_empresa', 'direccion', 'telefono', 'email')
    search_fields = ('nombre_empresa', 'rut_empresa')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(empresa, EmpresaAdmin)