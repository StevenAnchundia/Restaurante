from modelos import Producto, Cliente

class Restaurante:
    """
    Clase encargada de administrar productos y clientes.
    """

    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    # ==========================
    # PRODUCTOS
    # ==========================

    def registrar_producto(self, producto: Producto) -> bool:

        for producto_existente in self.productos:

            if producto_existente.codigo == producto.codigo:
                return False

        self.productos.append(producto)
        return True

    def listar_productos(self):

        if len(self.productos) == 0:
            print("\nNo existen productos registrados.\n")
            return

        print("\n========== PRODUCTOS ==========\n")

        # Polimorfismo
        for producto in self.productos:
            print(producto.mostrar_informacion())

        print()

    # ==========================
    # CLIENTES
    # ==========================

    def registrar_cliente(self, cliente: Cliente) -> bool:

        for cliente_existente in self.clientes:

            if (
                cliente_existente.identificacion
                == cliente.identificacion
            ):
                return False

        self.clientes.append(cliente)
        return True

    def listar_clientes(self):

        if len(self.clientes) == 0:
            print("\nNo existen clientes registrados.\n")
            return

        print("\n========== CLIENTES ==========\n")

        for cliente in self.clientes:
            print(cliente.mostrar_informacion())

        print()
