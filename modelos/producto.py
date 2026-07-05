class Producto:
    """Clase padre que representa un producto del restaurante."""

    def __init__(self, nombre: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.__precio = precio 
        self.disponible = disponible

    def obtener_precio(self):
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"

        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.__precio:.2f}")
        print(f"Estado: {estado}")
