import json
import os
from Cliente import Cliente


class GestorClientes:
    ARCHIVO_CLIENTES = "clientes.json"

    def __init__(self):
        # Inicializar self.clientes con una lista vacía
        self.clientes = []
        self.clientes = self.cargar_clientes()

    def agregar_cliente(self, cliente):
        # Convertir el cliente a diccionario antes de agregarlo
        self.clientes.append(cliente.to_dict())
        self.guardar_clientes()

    def obtener_clientes(self):
        # Convertir los diccionarios en objetos Cliente
        return [Cliente(**cliente) for cliente in self.clientes]

    def obtener_cliente_por_nombre(self, nombre):
        for cliente in self.clientes:
            if cliente["nombre"] == nombre:
                return Cliente(**cliente)  # Convertir el diccionario a Cliente
        return None

    def actualizar_cliente(self, cliente):
        for idx, cliente_existente in enumerate(self.clientes):
            if cliente_existente["nombre"] == cliente.nombre:
                # Convertir el objeto Cliente a diccionario antes de actualizar
                self.clientes[idx] = cliente.to_dict()
                self.guardar_clientes()
                return

    def eliminar_cliente(self, nombre):
        self.clientes = [cliente for cliente in self.clientes if cliente["nombre"] != nombre]
        self.guardar_clientes()

    def cargar_clientes(self):
        # Verificar si el archivo existe
        if not os.path.exists(self.ARCHIVO_CLIENTES):
            # Si no existe, crear el archivo con una lista vacía
            self.guardar_clientes()  # Esto inicializa el archivo con una lista vacía
            return []

        # Si el archivo existe, intentar cargar los clientes
        try:
            with open(self.ARCHIVO_CLIENTES, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            # Si ocurre un error al leer el archivo, reiniciar el archivo con una lista vacía
            self.guardar_clientes()  # Reescribir el archivo con una lista vacía
            return []

    def guardar_clientes(self):
        # Guardar los clientes en el archivo JSON
        with open(self.ARCHIVO_CLIENTES, "w") as file:
            json.dump(self.clientes, file, indent=4)
