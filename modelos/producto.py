class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.disponible = disponible

    def __str__(self):
        estado = "Sí" if self.disponible else "No"
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.cantidad_disponible}, Disponible: {estado}"

    def actualizar_stock(self, nueva_cantidad: int):
        self.cantidad_disponible = nueva_cantidad
        self.disponible = self.cantidad_disponible > 0
