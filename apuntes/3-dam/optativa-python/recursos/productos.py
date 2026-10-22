class Producto:
    
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre        

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

    def mostrar_info(self):
        return f"[Producto] Nombre: {self.nombre}, Precio: {self.precio:.2f} €, Stock: {self.stock}"