from django import forms
from .models import proveedor, producto

#Aquí se encuntran los formularios que se pasan en views.py

#Formularios de proveedores
class AddProveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = ['rut', 'nombre_proveedor', 'contacto']
        labels = {
            'rut': 'RUT',
            'nombre_proveedor': 'Nombre del Proveedor',
            'contacto': 'Contacto',
        }

class EditProveedorForm(forms.ModelForm):
    class Meta:
        model = proveedor
        fields = ['rut', 'nombre_proveedor', 'contacto']
        labels = {
            'rut': 'RUT',
            'nombre_proveedor': 'Nombre del Proveedor',
            'contacto': 'Contacto',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'type':'text', 'id': 'rut_editar'}),
            'nombre_proveedor': forms.TextInput(attrs={'type':'text', 'id': 'nombre_proveedor_editar'}),
            'contacto': forms.TextInput(attrs={'type':'text', 'id': 'contacto_editar'}),
        }


#Formularios de productos
class AddProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['sku', 'nombre_producto', 'imagen', 'descripcion', 'precio_costo', 'precio_venta', 'stock_actual', 'stock_minimo', 'id_proveedor']
        labels = {
            'sku': 'SKU',
            'nombre_producto': 'Nombre Producto',
            'imagen': 'Imagen',
            'descripcion': 'Descripción',
            'precio_costo': 'Precio de Costo',
            'precio_venta': 'Precio de Venta',
            'stock_actual': 'Stock Actual',
            'stock_minimo': 'Stock Mínimo',
            'id_proveedor': 'Proveedor',
        }

class EditProductoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['sku', 'nombre_producto', 'imagen', 'descripcion', 'precio_costo', 'precio_venta', 'stock_actual', 'stock_minimo', 'id_proveedor']
        labels = {
            'sku': 'SKU',
            'nombre_producto': 'Nombre Producto',
            'imagen': 'Imagen',
            'descripcion': 'Descripción',
            'precio_costo': 'Precio Costo',
            'precio_venta': 'Precio Venta',
            'stock_actual': 'Stock Actual',
            'stock_minimo': 'Stock Mínimo',
            'id_proveedor': 'Proveedor',
        }
        widgets = {
            'sku': forms.TextInput(attrs={'type':'text', 'id': 'sku_editar'}),
            'nombre_producto': forms.TextInput(attrs={'type':'text', 'id': 'nombre_producto_editar'}),
            'descripcion': forms.TextInput(attrs={'type':'text', 'id': 'descripcion_editar'}),
            'precio_costo': forms.NumberInput(attrs={'type':'number', 'id': 'precio_costo_editar'}),
            'precio_venta': forms.NumberInput(attrs={'type':'number', 'id': 'precio_venta_editar'}),
            'stock_actual': forms.NumberInput(attrs={'type':'number', 'id': 'stock_actual_editar'}),
            'stock_minimo': forms.NumberInput(attrs={'type':'number', 'id': 'stock_minimo_editar'}),
            'id_proveedor': forms.Select(attrs={'id': 'id_proveedor_editar'}),
        }