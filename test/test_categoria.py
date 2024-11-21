from app.producto import Producto
from app.categoria import Categoria
import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../app')))


def test_categoria_creation():
    categoria = Categoria(nombre="Categoría 1",
                          descripcion="Descripción de categoría 1")
    assert categoria.nombre == "Categoría 1"
    assert categoria.descripcion == "Descripción de categoría 1"


def test_add_producto():
    categoria = Categoria(nombre="Categoría 2",
                          descripcion="Descripción de categoría 2")
    producto = Producto(nombre="Producto 1", descripcion="Descripción 1",
                        precio=100.0, stock=50, categoria="Categoría 1")
    categoria.add_producto(producto)
    assert producto in categoria.productos


def test_remove_producto():
    categoria = Categoria(nombre="Categoría 3",
                          descripcion="Descripción de categoría 3")
    producto = Producto(nombre="Producto 2", descripcion="Descripción 2",
                        precio=150.0, stock=30, categoria="Categoría 3")
    categoria.add_producto(producto)
    categoria.remove_producto(producto)
    assert producto not in categoria.productos
