class Vehiculo:
    def __init__ (self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio


    def descripcion(self):
        return f"Vehículo: {self.marca} {self.modelo}, Año: {self.anio}"
    
    def arrancar(self):
        print(f"El Vehículo {self.marca} {self.modelo} está arrancado.")
    
