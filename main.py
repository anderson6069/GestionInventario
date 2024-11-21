import tkinter as tk
from tkinter import messagebox
from app.producto import Producto
from app.categoria import Categoria
from app.proveedor import Proveedor
from app.bodega import Bodega

categoria = Categoria("Electrónica", "Dispositivos electrónicos y gadgets")
proveedor = Proveedor("Tech Supplier", "Calle 123", "123456789")
bodega = Bodega("Central", "Ciudad", 100)


def agregar_producto():
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()
    try:
        precio = float(entry_precio.get())
        stock = int(entry_stock.get())
    except ValueError:
        messagebox.showerror(
            "Error", "Por favor ingresa valores numéricos válidos para precio y stock.")
        return

    if nombre and descripcion:
        # Crear el producto
        producto = Producto(nombre, descripcion, precio, stock)
        # Agregar a la categoría, proveedor y bodega
        categoria.agregar_producto(producto)
        proveedor.agregar_producto(producto)
        bodega.agregar_producto(producto, stock)

        messagebox.showinfo("Éxito", f"Producto {
                            nombre} agregado correctamente.")
        # Limpiar los campos
        entry_nombre.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_stock.delete(0, tk.END)
    else:
        messagebox.showwarning(
            "Advertencia", "Por favor ingresa todos los datos.")


def mostrar_info():
    # Mostrar información sobre la categoría, proveedor y bodega
    info = f"Categoría: {categoria.nombre}\nProductos: {
        len(categoria.productos)}\n\n"
    info += f"Proveedor: {proveedor.nombre}\nProductos: {
        len(proveedor.productos)}\n\n"
    info += f"Bodega: {bodega.nombre}\nProductos: {len(bodega.productos)}"
    messagebox.showinfo("Información", info)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Inventario")

# Campos de entrada
label_nombre = tk.Label(ventana, text="Nombre del Producto")
label_nombre.pack()

entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_descripcion = tk.Label(ventana, text="Descripción")
label_descripcion.pack()

entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack()

label_precio = tk.Label(ventana, text="Precio")
label_precio.pack()

entry_precio = tk.Entry(ventana)
entry_precio.pack()

label_stock = tk.Label(ventana, text="Stock")
label_stock.pack()

entry_stock = tk.Entry(ventana)
entry_stock.pack()

# Botón para agregar producto
boton_agregar = tk.Button(
    ventana, text="Agregar Producto", command=agregar_producto)
boton_agregar.pack()

# Botón para mostrar información de productos
boton_info = tk.Button(
    ventana, text="Mostrar Información", command=mostrar_info)
boton_info.pack()

# Ejecutar la interfaz
ventana.mainloop()
