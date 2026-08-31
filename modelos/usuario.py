class Usuario:
    """
    Clase que representa un usuario del restaurante.
    """

    def __init__(
        self,
        identificacion: str,
        nombre: str,
        correo: str
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.correo = correo

    # Identificación
    @property
    def identificacion(self) -> str:
        return self.__identificacion

    @identificacion.setter
    def identificacion(self, valor: str):
        if valor.strip() == "":
            raise ValueError("La identificación no puede estar vacía.")
        self.__identificacion = valor

    # Nombre

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        if valor.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor

    # Correo

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, valor: str):
        if "@" not in valor:
            raise ValueError("Correo electrónico inválido.")
        self.__correo = valor

    # Mostrar información

    def mostrar_informacion(self) -> str:
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )

    # JSON

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo
        }
