class Producto:

    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    def __str__(self):
        return (
            f"{self.codigo} - "
            f"{self.nombre} - "
            f"{self.categoria} - "
            f"${self.precio:.2f} - "
            f"Stock: {self.stock}"
        )
