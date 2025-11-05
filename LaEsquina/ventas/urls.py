from django.urls import path
from . import views
urlpatterns = [
    path('', views.ventas_view, name='Ventas'),
    # Urls de proveedores
    path('proveedores/', views.proveedores_view, name='Proveedores'),
    path('add_proveedor/', views.add_proveedor_view, name='AddProveedor'),
    path('edit_proveedor/', views.edit_proveedor_view, name='EditProveedor'),
    path('delete_proveedor/', views.delete_proveedor_view, name='DeleteProveedor'),

    # Urls de productos
    path('productos/', views.productos_view, name='Productos'),
    path('add_producto/', views.add_producto_view, name='AddProducto'),
    path('edit_producto/', views.edit_producto_view, name='EditProduct'),
    path('delete_producto/', views.delete_producto_view, name='DeleteProduct'),

    # Urls Ventas
    path('add_venta/',views.add_ventas.as_view(), name='AddVenta'),
    path('export/', views.export_pdf_view, name="ExportPDF" ),
    path('export/<id>/<iva>', views.export_pdf_view, name="ExportPDF" ),
    path('delete_venta/', views.delete_venta_view, name='DeleteVenta'),
]