class Cliente:
    def __init__(self, nombre, nif, direccion, telefono):
        self.nombre = nombre
        self.nif = nif
        self.direccion = direccion
        self.telefono = telefono

    def get_nombre(self):
        return self.nombre

    def get_nif(self):
        return self.nif

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_nif(self, nif):
        self.nif = nif

    def set_direccion(self, direccion):
        self.direccion = direccion

    def set_telefono(self, telefono):
        self.telefono = telefono
    


    def to_dict(self):
        # Método para convertir un objeto Cliente a diccionario
        return {
            'nombre': self.nombre,
            'nif': self.nif,
            'direccion': self.direccion,
            'telefono': self.telefono
        }
