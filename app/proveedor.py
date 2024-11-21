class Proveedor:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos = []

    def __str__(self):
        return f"Proveedor: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)
