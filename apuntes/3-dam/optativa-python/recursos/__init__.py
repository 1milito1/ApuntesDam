from .clientes import Cliente
from .productos import Producto
from .ventas import Venta
# Definición de la lista __all__ para exportar los módulos
# Esto es para que al importar el módulo solo se importen las clases Cliente, Producto y Venta
# y no otras clases o funciones que puedan estar en el módulo.
__all__ = ["Cliente", "Producto", "Venta"]
