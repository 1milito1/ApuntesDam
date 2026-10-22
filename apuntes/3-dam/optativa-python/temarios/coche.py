from .vehiculo import Vehiculo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def descripcion(self):
        info_base = super().descripcion()
        return f"{info_base}, puertas: {self.num_puertas}"
        
