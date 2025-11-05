/*$( document ).ready(function() {
    // Handler for .ready() called.
    alert('Todo bien');
  });*/

// Funciones productos

// Función para editar producto
function editarProduct(id_producto, sku, nombre_producto, descripcion, precio_costo, precio_venta, stock_actual, stock_minimo, id_proveedor) {
  document.getElementById("id_producto_editar").value = id_producto;
  document.getElementById("sku_editar").value = sku;
  document.getElementById("nombre_producto_editar").value = nombre_producto;
  document.getElementById("descripcion_editar").value = descripcion;
  document.getElementById("precio_costo_editar").value = precio_costo;
  document.getElementById("precio_venta_editar").value = precio_venta;
  document.getElementById("stock_actual_editar").value = stock_actual;
  document.getElementById("stock_minimo_editar").value = stock_minimo;
  document.getElementById("id_proveedor_editar").value = id_proveedor;
  if (servicio=='True'){
    document.getElementById('servicio_editar').checked=true;
  }
}

// Función eliminar producto
function eliminarProducto(id) {
  document.getElementById("id_producto_eliminar").value = id;
}


//Funciones ventas

//Función eliminar venta
function eliminarVenta(id) {
  document.getElementById("id_venta_eliminar").value = id;
}


//Funciones Proveedores

//Función para editar Proveedor
function editarPersonal(id_proveedor, rut, nombre_proveedor, contacto) {
  document.getElementById("id_personal_editar").value = id_proveedor;
  document.getElementById("rut_editar").value = rut;
  document.getElementById("nombre_proveedor_editar").value = nombre_proveedor;
  document.getElementById("contacto_editar").value = contacto;
}

//Función para eliminar Proveedor
function eliminarPersonal(id) {
  document.getElementById("id_personal_eliminar").value = id;
}

function borrarContent(){
  document.getElementById("search").value = "";
}

function activarEspera(){
  const btn = document.getElementById("btn");
  btn.innerHTML = 'Generando ... <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>';
  btn.disabled = true;
}

$(document).ready(function () {

  $('#myTable').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table2').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table3').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
});
 