class Bodega:
    def __init__(self, nombre, ubicacion, capacidad_maxima):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad_maxima = capacidad_maxima
        self.productos = []

    def __str__(self):
        return f"Bodega: {self.nombre}, Ubicación: {self.ubicacion}, Capacidad Máxima: {self.capacidad_maxima}"

    def agregar_producto(self, producto, cantidad):
        if len(self.productos) < self.capacidad_maxima:
            self.productos.append((producto, cantidad))
        else:
            print("No hay suficiente espacio en la bodega.")

    def retirar_producto(self, producto, cantidad):
        for p, cantidad_almacenada in self.productos:
            if p == producto:
                if cantidad <= cantidad_almacenada:
                    self.productos.remove((producto, cantidad_almacenada))
                    self.productos.append(
                        (producto, cantidad_almacenada - cantidad))
                else:
                    print("Cantidad a retirar mayor que la disponible.")
