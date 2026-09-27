class Producto:
    def __init__(self, id: int, nombre: str, precio: float, categoria: str, disponible: bool = True):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
            "disponible": self.disponible
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Producto":
        return cls(
            id=datos["id"],
            nombre=datos["nombre"],
            precio=datos["precio"],
            categoria=datos["categoria"],
            disponible=datos.get("disponible", True)
        )

    def __str__(self) -> str:
        estado = "✓" if self.disponible else "✗"
        return f"[{estado}] {self.nombre} — ${self.precio:.2f} ({self.categoria})"
