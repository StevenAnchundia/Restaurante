from modelos.producto import Producto


class Restaurante:
    """Administra los productos."""

    def __init__(self):
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def mostrar_productos(self):

        print("===== PRODUCTOS =====\n")

        for producto in self.productos:
            producto.mostrar_informacion()
            print("----------------------")
