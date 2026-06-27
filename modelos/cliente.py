class Cliente:
    def __init__(self, nombre: str, cedula: str, edad: int, activo: bool):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.activo = activo

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}, Edad: {self.edad}, Estado: {estado}"
