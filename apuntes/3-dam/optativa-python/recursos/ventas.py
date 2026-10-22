# Clase Venta

class Venta:

    # Constructor de la clase Venta
    def __init__(self, nom_cliente, nom_producto, imp_compra, stock_comprado):
        self.nom_cliente = nom_cliente
        self.nom_producto = nom_producto
        self.imp_compra = imp_compra
        self.stock_comprado = stock_comprado

    # Método para mostrar la información de la venta
    def mostrar_venta(self):
        return f"El Cliente: {self.nom_cliente} ha comprado {self.stock_comprado} unidades"\
               f" del producto {self.nom_producto}, por un importe de {self.imp_compra:.2f}€"

    # Método para realizar una venta            
    def realizar_venta(cliente, producto, cantidad):
        total = producto.precio * cantidad
        if cliente.saldo >= total and producto.stock >= cantidad:
            cliente.actualizar_saldo(-total)
            producto.actualizar_stock(-cantidad)
            print(f"Venta realizada: {cantidad} unidad(es) de {producto.nombre} a {cliente.nombre} por {total:.2f}€")
            
        elif cliente.saldo < total:
            return "Saldo insuficiente del cliente."
        elif producto.stock < cantidad:
            return "Stock insuficiente del producto."  
        return Venta(cliente.nombre, producto.nombre, total, cantidad)
