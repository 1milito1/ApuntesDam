from gestion_vehiculos.coche import Coche
from gestion_vehiculos.moto import Moto 

mi_coche = Coche("Peugeot", "2008", 2015, 5)
mi_moto = Moto("Voge", "525dsx", 2025, "trial")


print(mi_coche.descripcion())
mi_coche.arrancar()

print(mi_moto.descripcion())
mi_moto.arrancar()