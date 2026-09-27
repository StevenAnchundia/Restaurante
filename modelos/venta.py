from datetime import datetime


class Venta:
    def __init__(self, id: int, usuario_id: int, usuario_nombre: str,
                 producto_id: int, producto_nombre: str,
                 precio_unitario: float, cantidad: int, fecha: str = None):
        self.id = id
        self.usuario_id = usuario_id
        self.usuario_nombre = usuario_nombre
        self.producto_id = producto_id
        self.producto_nombre = producto_nombre
        self.precio_unitario = precio_unitario
        self.cantidad = cantidad
        self.total = round(precio_unitario * cantidad, 2)
        self.fecha = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "usuario_nombre": self.usuario_nombre,
            "producto_id": self.producto_id,
            "producto_nombre": self.producto_nombre,
            "precio_unitario": self.precio_unitario,
            "cantidad": self.cantidad,
            "total": self.total,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos: dict) -> "Venta":
        venta = cls(
            id=datos["id"],
            usuario_id=datos["usuario_id"],
            usuario_nombre=datos["usuario_nombre"],
            producto_id=datos["producto_id"],
            producto_nombre=datos["producto_nombre"],
            precio_unitario=datos["precio_unitario"],
            cantidad=datos["cantidad"],
            fecha=datos.get("fecha")
        )
        venta.total = datos.get("total", round(venta.precio_unitario * venta.cantidad, 2))
        return venta

    def __str__(self) -> str:
        return (f"Venta #{self.id} | {self.usuario_nombre} | "
                f"{self.producto_nombre} x{self.cantidad} | "
                f"${self.total:.2f} | {self.fecha}")
