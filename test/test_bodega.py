from app.producto import Producto
from app.bodega import Bodega
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../app')))


def test_bodega_creation():
    bodega = Bodega(nombre="Bodega 1", ubicacion="Ubicación 1",
                    capacidad_maxima=100)
    assert bodega.nombre == "Bodega 1"
    assert bodega.ubicacion == "Ubicación 1"
    assert bodega.capacidad_maxima == 100


def test_agregar_producto_a_bodega():
    bodega = Bodega(nombre="Bodega 2", ubicacion="Ubicación 2",
                    capacidad_maxima=100)
    producto = Producto(nombre="Producto 1", descripcion="Descripción 1",
                        precio=100.0, stock=50, categoria="Categoría 1")
    bodega.agregar_producto(producto)
    assert producto in bodega.productos


def test_quitar_producto_de_bodega():
    bodega = Bodega(nombre="Bodega 3", ubicacion="Ubicación 3",
                    capacidad_maxima=100)
    producto = Producto(nombre="Producto 2", descripcion="Descripción 2",
                        precio=150.0, stock=30, categoria="Categoría 2")
    bodega.agregar_producto(producto)
    bodega.quitar_producto(producto)
    assert producto not in bodega.productos
