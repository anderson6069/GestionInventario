class Categoria:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def __str__(self):
        return f"Categoría: {self.nombre}, Descripción: {self.descripcion}"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
