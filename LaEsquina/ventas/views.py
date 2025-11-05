from django.shortcuts import render, redirect
from django.contrib import messages
from .models import proveedor, producto, venta, detalle_venta, usuario
from .forms import AddProveedorForm, EditProveedorForm, AddProductoForm, EditProductoForm
from django.views.generic import ListView
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from django.conf import settings
import os
import io
from xhtml2pdf import pisa
import json

# Create your views here.



#Vistas de proveedores
def proveedores_view(request):
    Proveedor = proveedor.objects.all()
    form_personal = AddProveedorForm()
    form_editar = EditProveedorForm()
    context = {
        'proveedor': Proveedor,
        'form_personal': form_personal,
        'form_editar': form_editar
    }
    return render(request, 'proveedores.html',context)

def add_proveedor_view(request):
    if request.method == 'POST':
        form = AddProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, 'Error al agregar el proveedor')
                return redirect('Proveedores')
    return redirect('Proveedores')

def edit_proveedor_view(request):
    if request.method == 'POST':
            proveedor_id = proveedor.objects.get(pk=int(request.POST.get('id_personal_editar')))
            form = EditProveedorForm(request.POST, request.FILES, instance= proveedor_id)
            if form.is_valid():
                    form.save()
    return redirect('Proveedores')

def delete_proveedor_view(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('id_personal_eliminar')
        if proveedor_id:
                proveedor_obj = proveedor.objects.get(pk=int(proveedor_id))
                proveedor_obj.delete()
    return redirect('Proveedores')

#Vistas de productos
def productos_view(request):
    Productos = producto.objects.all()
    form_add = AddProductoForm()
    form_editar = EditProductoForm()
    context = {
        'productos': Productos,
        'form_add': form_add
        ,'form_editar': form_editar
    }
    return render(request, 'productos.html',context)

def add_producto_view(request):
    if request.method == 'POST':
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, 'Error al agregar productos')
                return redirect('Productos')
    return redirect('Productos')

def edit_producto_view(request):
    if request.method == 'POST':
            producto_id = producto.objects.get(pk=int(request.POST.get('id_producto_editar')))
            form = EditProductoForm(request.POST, request.FILES, instance= producto_id)
            if form.is_valid():
                    form.save()
    return redirect('Productos')

def delete_producto_view(request):
    if request.method == 'POST':
        producto_id = request.POST.get('id_producto_eliminar')
        if producto_id:
                producto_obj = producto.objects.get(pk=int(producto_id))
                producto_obj.delete()
    return redirect('Productos')

#Vista ventas
def ventas_view(request):
    ventas = venta.objects.all()
    num_ventas = len(ventas)
    context = {
        'ventas':ventas,
        'num_ventas':num_ventas
    }
    return render(request, 'ventas.html', context)

class add_ventas(ListView):
    template_name = 'add_ventas.html'
    model = venta

    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    """
    def get_queryset(self):
        return ProductosPreventivo.objects.filter(
            preventivo=self.kwargs['id']
        )
    """
    def post(self, request,*ars, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'autocomplete':
                # Autocomplete debe devolver una lista
                results = []
                term = request.POST.get('term', '')
                qs = producto.objects.filter(Q(nombre_producto__icontains=term) | Q(descripcion__icontains=term))[0:10]
                for i in qs:
                    item = {
                        'id': i.id_producto,
                        'descripcion': i.nombre_producto,
                        'precio': i.precio_venta,
                        'value': i.nombre_producto,
                    }
                    results.append(item)
                return JsonResponse(results, safe=False)
            elif action == 'save':
                #Validamos información
                total_pagado = float(request.POST['efectivo']) + float(request.POST['tarjeta']) + float(request.POST['transferencia']) + float(request.POST['otro']) + float(request.POST['vales'])
                datos = json.loads(request.POST.get('verts', '{}'))
                total = float(datos.get('total', 0))
                desglosar = int(request.POST.get('desglosar', 0))
                
                # Obtener usuario (por ahora usaremos el primer usuario)
                usuario_actual = usuario.objects.first()

                # Validar stock antes de crear la venta
                for item in datos.get('products', []):
                    prod_id = item.get('id') if isinstance(item, dict) else None
                    if prod_id is None:
                        prod_id = item.get('id_producto') if isinstance(item, dict) else None
                    try:
                        producto_obj = producto.objects.get(pk=int(prod_id))
                    except Exception:
                        data['error'] = f"Producto con id {prod_id} no encontrado"
                        return JsonResponse(data, safe=False)
                    cantidad = int(item.get('cantidad', 0))
                    if producto_obj.stock_actual < cantidad:
                        data['error'] = f"Stock insuficiente para '{producto_obj.nombre_producto}'. Disponible: {producto_obj.stock_actual}"
                        return JsonResponse(data, safe=False)
                        


                #Guardar venta
                nueva_venta = venta(
                    total_venta=total,
                    id_usuario=usuario_actual
                )
                nueva_venta.save()

                #Guardar detalles de la venta
                for item in datos['products']:
                    producto_obj = producto.objects.get(pk=int(item['id']))
                    detalle = detalle_venta(
                        id_venta=nueva_venta,
                        id_producto=producto_obj,
                        cantidad=int(item['cantidad']),
                        precio_unitario_venta=float(item['precio'])
                    )
                    detalle.save()
                    
                    # Actualizar stock
                    producto_obj.stock_actual -= int(item['cantidad'])
                    producto_obj.save()

                data['venta_id'] = nueva_venta.id_venta
                data['desglosar'] = desglosar
                data['success'] = True

            else:
                data['error'] = "Ha ocurrido un error"
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data,safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos_lista'] = producto.objects.all()
        return context
    
def delete_venta_view(request):
    if request.method == 'POST':
        venta_id = request.POST.get('id_venta_eliminar')
        if venta_id:
                venta_obj = venta.objects.get(pk=int(venta_id))
                venta_obj.delete()
    return redirect('Ventas')

def export_pdf_view(request, id, iva):
    #print(id)
    template = get_template("ticket.html")
    #print(id)
    subtotal = 0 
    iva_suma = 0 

    venta_pdf = venta.objects.get(pk=int(id))
    datos = detalle_venta.objects.filter(id_venta=venta_pdf)
    # Usamos directamente los objetos del detalle_venta
    items_con_subtotal = datos  # No necesitamos crear una nueva lista
    for i in datos:
        item_subtotal = float(i.precio_unitario_venta) * float(i.cantidad)
        subtotal = subtotal + item_subtotal
        if iva == "1":
            iva_suma = iva_suma + (item_subtotal * 0.19)

    from .models import empresa as EmpresaModel
    datos_empresa = EmpresaModel.objects.first()
    context ={
        'num_ticket': id,
        'iva': iva,
        'fecha': venta_pdf.fecha_hora,
        'items': items_con_subtotal, 
        'total': venta_pdf.total_venta, 
        'empresa': datos_empresa,
        'subtotal': subtotal,
        'iva_suma': iva_suma,
    }
    html_template = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response["Content-Disposition"] = 'inline; filename="ticket.pdf"'
    # Si tienes CSS externo, usa rutas absolutas y pásalas en el HTML o incrústalo.
    pisa_status = pisa.CreatePDF(src=html_template, dest=response, encoding='utf-8')
    if pisa_status.err:
        return HttpResponse('Error al generar PDF', status=500)
    return response