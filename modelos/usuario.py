class Usuario:
    def __init__(self, id: int, nombre: str, usuario: str, contrasena: str, rol: str):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contrasena": self.contrasena,
            "rol": self.rol
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Usuario":
        return cls(
            id=datos["id"],
            nombre=datos["nombre"],
            usuario=datos["usuario"],
            contrasena=datos["contrasena"],
            rol=datos.get("rol", "mesero")
        )

    def __str__(self) -> str:
        return f"{self.nombre} ({self.rol})"
