# Ejercicio 1 Creando una clase coche


class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def arrancar(self):
        print(f"El coche {self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        print (f"El coche {self.marca} {self.modelo} se ha detenido.")

# Prueba de funcionalidad
print ("\n --- Prueba del Ejercicio 1 ---")
coche1 = Coche("Peugeot", "2008", 2016) # Creamos una instancia
# Llamamos a sus métodos
coche1.arrancar()
coche1.detener()


# Ejercico 2 encapsulación y métodos getters y setters

class Coche:
    def __init__(self, marca ,modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.__kilometraje = 0 # Atributo privado
    def get_kilometraje(self):
        return f"Kilometraje actual {self.__kilometraje} km"
    
    def set_kilometraje(self, nuevo_km):
        if nuevo_km > self.__kilometraje:
            self.__kilometraje = nuevo_km
            print (f"kimotregaje actualizado a {nuevo_km} km")
        else:
            print("No se puede reducir el kilometraje.")

#Prueba de funcionalidad del ejercicio 2
print ("\n --- Prueba del Ejercicio 2 ---")
coche_encapsulado = Coche("Audi", "A4", 2018)
print(coche_encapsulado.get_kilometraje())  # Obtener kilometraje inicial
coche_encapsulado.set_kilometraje(150)    # Actualizar kilometrometaje
print(coche_encapsulado.get_kilometraje())  # Obtener kilometraje actualizado
coche_encapsulado.set_kilometraje(100)    # Intentar reducir kilometraje


# Ejercico 3 Herencia y sobrescritura de métodos

class Electrico(Coche):
    def __init__ (self, marca, modelo, anio, bateria):
        super().__init__(marca, modelo, anio)
        self.bateria = bateria
    
    def arrancar(self):
        print(f"La bateria tiene una capacidad de {self.bateria} kWh.")
        print(f"El coche eléctrico {self.marca} {self.modelo} ha arrancado silenciosamente.")


# Prueba de funcionalidad del ejercicio 3
print ("\n --- Prueba del Ejercicio 3 ---")
coche_electrico = Electrico("Tesla", "Model 3", 2024, 100)
coche_electrico.arrancar()


# Ejercico 4 Método especial y polimorfismo

class Coche:
    def __init__ (self, marca,modelo, anio):
        self.marca = marca
        self.modelo =modelo
        self.anio = anio
        self.__kilometraje = 1000
    def get_kilometraje(self):
        return self
    def __str__(self):
        return f"Coche: {self.marca} {self.modelo} {self.anio} kilometraje: {self.__kilometraje} km"
    
class Electrico(Coche):
    def __init__ (self, marca, modelo, anio, bateria):
        super().__init__(marca, modelo, anio)
        self.bateria = bateria
        self._Coche__kilometraje = 900
    def __str__(self):
        return f"coche eléctrico: {self.marca} {self.modelo} {self.anio} kilometraje: {self._Coche__kilometraje} km Bateria: {self.bateria} kWh"
        
# Prueba de funcionalidad del ejercicio 4
print ("\n --- Prueba del Ejercicio 4 ---")
coche_polimorfico = Coche("Ford", "Focus", 2020)
coche_polimorfico_electrico = Electrico("Nissan", "Leaf", 2021, 40)
print(coche_polimorfico)
print(coche_polimorfico_electrico)


# Ejercico 5 gestion de flota

class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_coche(self, coche):
        
        if isinstance(coche, Coche):
            self.vehiculos.append(coche)
            print(f"Vehículo {coche.marca} añadido a la flota.")
        else:
            print("Error: Solo se pueden añadir objetos de tipo Coche a la flota.")

    def mostrar_flota(self):
        print("\nMi flota es:")
        for vehiculo in self.vehiculos:
            print(vehiculo)

# Prueba de funcionalidad del ejercicio 5
print ("\n --- Prueba del Ejercicio 5 ---")
mi_flota = Flota()
mi_flota.agregar_coche(Coche("BMW", "X3", 2019))
mi_flota.agregar_coche(Electrico("Chevrolet", "Bolt", 2022, 60))
mi_flota.mostrar_flota()

# Ejercicio 6 registro de vehículos con mixin

from datetime import datetime

class AuditMixin:
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.fecha_creacion = datetime.now()

    def mostrar_auditoria(self):
        print(f"Registro: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}")

class LoggingMixin:
    def log_registro(self, nombre):
        print(f"LOG: Vehículo '{nombre}' registrado con éxito.")


class CocheCompleto(AuditMixin, LoggingMixin, Coche):
    def __init__(self, marca, modelo, anio):
        # super() inicializa Coche y AuditMixin automáticamente
        super().__init__(marca, modelo, anio)
        self.log_registro(f"{marca} {modelo}")

# Prueba de funcionalidad del ejercicio 6

print("\n--- Prueba del Ejercicio 6 (Corregido) ---")
coche_final = CocheCompleto("Volkswagen", "Golf", 2023)
coche_final.mostrar_auditoria()
print(coche_final)
                          




