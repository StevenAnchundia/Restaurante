class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, nombre: str, categoria: str,
                 precio: float, disponible: bool):

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # Nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    # Categoría
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        if valor.strip() == "":
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = valor

    # Precio
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = valor

    def mostrar_informacion(self):

        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"{estado}"
        )
