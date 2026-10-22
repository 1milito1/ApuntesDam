class Cliente:

    def __init__(self, nombre, correo, saldo):
        self.nombre = nombre
        self.correo = correo
        self.saldo = saldo

    def actualizar_saldo(self, cantidad):
        self.saldo += cantidad

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo
    
    def nuevo_saldo(self, nuevo_saldo):
        self.saldo = nuevo_saldo

    def mostrar_info(self):
        return f"[Cliente] Nombre: {self.nombre}, Correo: {self.correo}, Saldo: {self.saldo:.2f}"