from app.producto import Producto
import pytest
import sys
import os


sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../app')))


def test_producto_creation():
    producto = Producto(nombre="Producto 1",
                        descripcion="Descripción 1", precio=100.0, stock=50)
    assert producto.nombre == "Producto 1"
    assert producto.descripcion == "Descripción 1"
    assert producto.precio == 100.0
    assert producto.stock == 50


def test_agregar_stock():
    producto = Producto(nombre="Producto 2",
                        descripcion="Descripción 2", precio=200.0, stock=50)
    producto.agregar_stock(30)
    assert producto.stock == 80  # El stock debería aumentar a 80


def test_retirar_stock():
    producto = Producto(nombre="Producto 3",
                        descripcion="Descripción 3", precio=300.0, stock=50)
    producto.retirar_stock(20)
    assert producto.stock == 30  # El stock debería reducirse a 30

    # Probar el caso en el que no hay suficiente stock
    producto.retirar_stock(40)  # Esto debería imprimir un mensaje de error
    assert producto.stock == 30  # El stock no debería cambiar


def test_calcular_valor_stock():
    producto = Producto(nombre="Producto 4",
                        descripcion="Descripción 4", precio=100.0, stock=50)
    valor_stock = producto.calcular_valor_stock()
    assert valor_stock == 5000.0  # 100 * 50 = 5000
