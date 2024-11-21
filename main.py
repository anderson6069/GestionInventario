import tkinter as tk
from tkinter import messagebox
from app.producto import Producto
from app.categoria import Categoria
from app.proveedor import Proveedor
from app.bodega import Bodega

# Funciones de interfaz


def agregar_producto():
    nombre = entry_nombre.get()
    descripcion = entry_descripcion.get()
    precio = float(entry_precio.get())
    stock = int(entry_stock.get())
    producto = Producto(nombre, descripcion, precio, stock)
    productos_listbox.insert(tk.END, producto)


def agregar_categoria():
    nombre = entry_categoria_nombre.get()
    descripcion = entry_categoria_descripcion.get()
    categoria = Categoria(nombre, descripcion)
    categorias_listbox.insert(tk.END, categoria)


def agregar_proveedor():
    nombre = entry_proveedor_nombre.get()
    direccion = entry_proveedor_direccion.get()
    telefono = entry_proveedor_telefono.get()
    proveedor = Proveedor(nombre, direccion, telefono)
    proveedores_listbox.insert(tk.END, proveedor)


def agregar_bodega():
    nombre = entry_bodega_nombre.get()
    ubicacion = entry_bodega_ubicacion.get()
    capacidad_maxima = int(entry_bodega_capacidad.get())
    bodega = Bodega(nombre, ubicacion, capacidad_maxima)
    bodegas_listbox.insert(tk.END, bodega)


def mostrar_producto_seleccionado(event):
    index = productos_listbox.curselection()
    if index:
        producto = productos_listbox.get(index)
        messagebox.showinfo("Producto", str(producto))


def mostrar_categoria_seleccionada(event):
    index = categorias_listbox.curselection()
    if index:
        categoria = categorias_listbox.get(index)
        messagebox.showinfo("Categoría", str(categoria))


def mostrar_proveedor_seleccionado(event):
    index = proveedores_listbox.curselection()
    if index:
        proveedor = proveedores_listbox.get(index)
        messagebox.showinfo("Proveedor", str(proveedor))


def mostrar_bodega_seleccionada(event):
    index = bodegas_listbox.curselection()
    if index:
        bodega = bodegas_listbox.get(index)
        messagebox.showinfo("Bodega", str(bodega))


# Crear ventana principal
root = tk.Tk()
root.title("Gestión de Inventario")

# Crear campos de entrada para Producto
label_nombre = tk.Label(root, text="Nombre del Producto:")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

label_descripcion = tk.Label(root, text="Descripción del Producto:")
label_descripcion.grid(row=1, column=0)
entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=1, column=1)

label_precio = tk.Label(root, text="Precio del Producto:")
label_precio.grid(row=2, column=0)
entry_precio = tk.Entry(root)
entry_precio.grid(row=2, column=1)

label_stock = tk.Label(root, text="Stock del Producto:")
label_stock.grid(row=3, column=0)
entry_stock = tk.Entry(root)
entry_stock.grid(row=3, column=1)

# Botón para agregar Producto
btn_agregar_producto = tk.Button(
    root, text="Agregar Producto", command=agregar_producto)
btn_agregar_producto.grid(row=4, column=0, columnspan=2)

# Crear Listbox para mostrar Productos
productos_listbox = tk.Listbox(root)
productos_listbox.grid(row=5, column=0, columnspan=2, sticky="nsew")
productos_listbox.bind("<Double-1>", mostrar_producto_seleccionado)

# Crear campos de entrada para Categoria
label_categoria_nombre = tk.Label(root, text="Nombre de la Categoría:")
label_categoria_nombre.grid(row=6, column=0)
entry_categoria_nombre = tk.Entry(root)
entry_categoria_nombre.grid(row=6, column=1)

label_categoria_descripcion = tk.Label(
    root, text="Descripción de la Categoría:")
label_categoria_descripcion.grid(row=7, column=0)
entry_categoria_descripcion = tk.Entry(root)
entry_categoria_descripcion.grid(row=7, column=1)

# Botón para agregar Categoria
btn_agregar_categoria = tk.Button(
    root, text="Agregar Categoría", command=agregar_categoria)
btn_agregar_categoria.grid(row=8, column=0, columnspan=2)

# Crear Listbox para mostrar Categorias
categorias_listbox = tk.Listbox(root)
categorias_listbox.grid(row=9, column=0, columnspan=2, sticky="nsew")
categorias_listbox.bind("<Double-1>", mostrar_categoria_seleccionada)

# Crear campos de entrada para Proveedor
label_proveedor_nombre = tk.Label(root, text="Nombre del Proveedor:")
label_proveedor_nombre.grid(row=10, column=0)
entry_proveedor_nombre = tk.Entry(root)
entry_proveedor_nombre.grid(row=10, column=1)

label_proveedor_direccion = tk.Label(root, text="Dirección del Proveedor:")
label_proveedor_direccion.grid(row=11, column=0)
entry_proveedor_direccion = tk.Entry(root)
entry_proveedor_direccion.grid(row=11, column=1)

label_proveedor_telefono = tk.Label(root, text="Teléfono del Proveedor:")
label_proveedor_telefono.grid(row=12, column=0)
entry_proveedor_telefono = tk.Entry(root)
entry_proveedor_telefono.grid(row=12, column=1)

# Botón para agregar Proveedor
btn_agregar_proveedor = tk.Button(
    root, text="Agregar Proveedor", command=agregar_proveedor)
btn_agregar_proveedor.grid(row=13, column=0, columnspan=2)

# Crear Listbox para mostrar Proveedores
proveedores_listbox = tk.Listbox(root)
proveedores_listbox.grid(row=14, column=0, columnspan=2, sticky="nsew")
proveedores_listbox.bind("<Double-1>", mostrar_proveedor_seleccionado)

# Crear campos de entrada para Bodega
label_bodega_nombre = tk.Label(root, text="Nombre de la Bodega:")
label_bodega_nombre.grid(row=15, column=0)
entry_bodega_nombre = tk.Entry(root)
entry_bodega_nombre.grid(row=15, column=1)

label_bodega_ubicacion = tk.Label(root, text="Ubicación de la Bodega:")
label_bodega_ubicacion.grid(row=16, column=0)
entry_bodega_ubicacion = tk.Entry(root)
entry_bodega_ubicacion.grid(row=16, column=1)

label_bodega_capacidad = tk.Label(root, text="Capacidad Máxima de la Bodega:")
label_bodega_capacidad.grid(row=17, column=0)
entry_bodega_capacidad = tk.Entry(root)
entry_bodega_capacidad.grid(row=17, column=1)

# Botón para agregar Bodega
btn_agregar_bodega = tk.Button(
    root, text="Agregar Bodega", command=agregar_bodega)
btn_agregar_bodega.grid(row=18, column=0, columnspan=2)

# Crear Listbox para mostrar Bodegas
bodegas_listbox = tk.Listbox(root)
bodegas_listbox.grid(row=19, column=0, columnspan=2, sticky="nsew")
bodegas_listbox.bind("<Double-1>", mostrar_bodega_seleccionada)

# Iniciar la aplicación
root.mainloop()
