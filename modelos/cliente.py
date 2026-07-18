from dataclasses import dataclass

@dataclass
class Cliente:
    """
    Clase que representa un cliente.
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
