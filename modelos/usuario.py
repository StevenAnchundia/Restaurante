from dataclasses import dataclass

@dataclass
class Usuario:
    """
    Representa un usuario registrado en el sistema.
    """

    identificacion: str
    nombre: str
    correo: str

    def mostrar_informacion(self) -> str:

        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )
