from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    # PRODUCTOS

    def registrar_producto(self, producto: Producto):
        self.productos.append(producto)

    def listar_productos(self):

        if not self.productos:
            print("No existen productos.")
            return

        for producto in self.productos:
            print(producto.mostrar_informacion())

    def buscar_producto(self, nombre: str):

        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print(producto.mostrar_informacion())
                return

        print("Producto no encontrado.")

    # CLIENTES

    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def listar_clientes():

        if not self.clientes:
            print("No existen clientes.")
            return

        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente(self, id_cliente):

        for cliente in self.clientes:

            if cliente.id_cliente == id_cliente:
                print(cliente)
                return

        print("Cliente no encontrado.")
