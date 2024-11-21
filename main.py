from app.categoria import Categoria
from app.proveedor import Proveedor
from app.producto import Producto
from app.bodega import Bodega
# Crear productos
producto1 = Producto("Laptop", "Laptop de alta gama", 1000, 10, "Electrónica")
producto2 = Producto("Teclado", "Teclado mecánico", 150, 20, "Accesorios")

# Crear categorías
categoria1 = Categoria("Electrónica", "Productos electrónicos")
categoria2 = Categoria("Accesorios", "Accesorios para computadoras")

# Agregar productos a las categorías
categoria1.agregar_producto(producto1)
categoria2.agregar_producto(producto2)

# Crear proveedor
proveedor = Proveedor("Proveedor A", "Calle Falsa 123", "555-1234")
proveedor.agregar_producto(producto1)
proveedor.agregar_producto(producto2)

# Crear bodega
bodega = Bodega("Bodega Central", "Ubicación A1", 100)

# Agregar productos a la bodega
bodega.agregar_producto(producto1, 10)
bodega.agregar_producto(producto2, 20)

# Mostrar productos almacenados en la bodega
print("Productos en la bodega:")
print(bodega.listar_productos())

# Vender productos
print("\nVendiendo productos...")
bodega.vender_producto("Laptop", 5)  # Vende 5 laptops
bodega.vender_producto("Teclado", 5)  # Vende 5 teclados

# Mostrar productos después de la venta
print("\nProductos en la bodega después de la venta:")
print(bodega.listar_productos())

# Intentar vender un producto con un stock insuficiente
print("\nIntentando vender un producto con stock insuficiente:")
bodega.vender_producto("Laptop", 10)  # No hay suficiente stock
