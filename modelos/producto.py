
class Producto:
    """
    Clase que representa un producto del restaurante.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float
    ):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    # Código

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, valor: str):
        if valor.strip() == "":
            raise ValueError("El código no puede estar vacío.")
        self.__codigo = valor

    # Nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    # Categoría

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, valor: str):
        if valor.strip() == "":
            raise ValueError("La categoría no puede estar vacía.")
        self.__categoria = valor

    # Precio

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = valor

    # Mostrar información

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )

    # Convertir a diccionario

    def to_dict(self) -> dict:
        """
        Convierte el objeto Producto en un diccionario
        para poder almacenarlo en formato JSON.
        """
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }
