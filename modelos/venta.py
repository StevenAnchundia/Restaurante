class Venta:
    """
    Representa una venta realizada por un usuario.
    """

    def __init__(
        self,
        usuario_id: str,
        producto_codigo: str,
        cantidad: int
    ):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = cantidad

    @property
    def usuario_id(self):
        return self.__usuario_id

    @usuario_id.setter
    def usuario_id(self, valor):
        if valor.strip() == "":
            raise ValueError("El usuario es obligatorio.")
        self.__usuario_id = valor

    @property
    def producto_codigo(self):
        return self.__producto_codigo

    @producto_codigo.setter
    def producto_codigo(self, valor):
        if valor.strip() == "":
            raise ValueError("El código del producto es obligatorio.")
        self.__producto_codigo = valor

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor):
        if valor <= 0:
            raise ValueError("Cantidad inválida.")
        self.__cantidad = valor

    def mostrar_informacion(self):
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def to_dict(self):
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad
        }
