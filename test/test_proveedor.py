import os
from app.proveedor import Proveedor
import pytest
import sys
print(sys.path)

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../app')))


def test_proveedor_creation():
    proveedor = Proveedor(nombre="Proveedor 1",
                          direccion="Calle 123", telefono="123456789")
    assert proveedor.nombre == "Proveedor 1"
    assert proveedor.direccion == "Calle 123"
    assert proveedor.telefono == "123456789"


def test_agregar_producto():
    proveedor = Proveedor(nombre="Proveedor 2",
                          direccion="Calle 456", telefono="987654321")
    producto = Producto(nombre="Producto 1", descripcion="Descripción 1",
                        precio=100.0, stock=50, categoria="Categoría 1")
    proveedor.agregar_producto(producto)
    assert producto in proveedor.productos


def test_quitar_producto():
    proveedor = Proveedor(nombre="Proveedor 3",
                          direccion="Calle 789", telefono="456123789")
    producto = Producto(nombre="Producto 2", descripcion="Descripción 2",
                        precio=150.0, stock=30, categoria="Categoría 2")
    proveedor.agregar_producto(producto)
    proveedor.quitar_producto(producto)
    assert producto not in proveedor.productos
