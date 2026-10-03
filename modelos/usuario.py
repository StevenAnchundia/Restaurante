class Usuario:

    ROL_ADMINISTRADOR = "Administrador"
    ROL_EMPLEADO = "Empleado"
    ROL_CLIENTE = "Cliente"

    ROLES = (ROL_ADMINISTRADOR, ROL_EMPLEADO, ROL_CLIENTE)
    ROLES_GESTIONABLES = (ROL_EMPLEADO, ROL_CLIENTE)

    _ROLES_LEGADOS = {
        "administrador": ROL_ADMINISTRADOR,
        "admin": ROL_ADMINISTRADOR,
        "empleado": ROL_EMPLEADO,
        "mesero": ROL_EMPLEADO,
        "cajero": ROL_EMPLEADO,
        "cliente": ROL_CLIENTE,
    }

    def __init__(self, id: int, nombre: str, usuario: str, contrasena: str, rol: str):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = self.normalizar_rol(rol)

    @classmethod
    def normalizar_rol(cls, rol: str) -> str:
        """Devuelve el rol en su forma canónica; si no se reconoce, lo deja igual."""
        clave = (rol or "").strip().lower()
        return cls._ROLES_LEGADOS.get(clave, (rol or "").strip())

    def es_administrador(self) -> bool:
        return self.rol == self.ROL_ADMINISTRADOR

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
            rol=datos.get("rol", cls.ROL_EMPLEADO)
        )

    def __str__(self) -> str:
        return f"{self.nombre} ({self.rol})"
