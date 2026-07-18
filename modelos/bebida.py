from modelos.producto import Producto

class Bebida(Producto):
    """
    Clase hija que representa una bebida.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamano: str
    ):

        super().__init__(
            codigo,
            nombre,
            categoria,
            precio
        )

        self.tamano = tamano

    @property
    def tamano(self) -> str:
        return self.__tamano

    @tamano.setter
    def tamano(self, valor: str):

        if valor.strip() == "":
            raise ValueError("El tamaño no puede estar vacío.")

        self.__tamano = valor

    def mostrar_informacion(self) -> str:

        return (
            super().mostrar_informacion()
            + f" | Tamaño: {self.tamano}"
        )
