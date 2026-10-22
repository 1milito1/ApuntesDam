from .vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self,marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        opciones_validas = ["deportiva", "scooter", "naked"]

        if tipo.lower() in opciones_validas:
            self.tipo = tipo
        else:
            print(f"Tipo de moto no válido. Se asignará 'deportiva'")
            self.tipo = "deportiva"

    def descripcion(self):
        info_base = super().descripcion()
        return f"{info_base}, tipo: {self.tipo}"
    
