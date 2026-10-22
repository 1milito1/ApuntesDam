class Concepto:
    def __init__(self, cantidad, descripcion, precio):
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.precio = precio

    def get_cantidad(self):
        return self.cantidad

    def get_descripcion(self):
        return self.descripcion

    def get_precio(self):
        return self.precio
