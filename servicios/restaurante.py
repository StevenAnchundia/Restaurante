from modelos import Producto, Usuario, Venta


class Restaurante:
    """
    Clase encargada de administrar los productos,
    usuarios y ventas del sistema.
    """

    def __init__(self):
        # Colecciones
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []
        self.ventas: list[Venta] = []

    # =====================================
    # PRODUCTOS
    # =====================================

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un producto si el código no existe.
        """

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        """
        Busca un producto por código.
        """

        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> bool:
        """
        Actualiza un producto existente.
        """

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """
        Elimina un producto por código.
        """

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self.productos.remove(producto)

        return True

    def listar_productos(self):

        if not self.productos:
            print("\nNo existen productos registrados.\n")
            return

        print("\n========== PRODUCTOS ==========\n")

        for producto in self.productos:
            print(producto.mostrar_informacion())

        print()

    # =====================================
    # USUARIOS
    # =====================================

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un usuario.
        """

        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self.usuarios.append(usuario)

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:
        """
        Busca un usuario por identificación.
        """

        for usuario in self.usuarios:

            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self):

        if not self.usuarios:
            print("\nNo existen usuarios registrados.\n")
            return

        print("\n========== USUARIOS ==========\n")

        for usuario in self.usuarios:
            print(usuario.mostrar_informacion())

        print()

    # =====================================
    # VENTAS
    # =====================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> tuple[bool, str]:
        """
        Realiza una venta.
        """

        usuario = self.buscar_usuario(
            identificacion_usuario
        )

        if usuario is None:
            return False, "El usuario no existe."

        producto = self.buscar_producto(
            codigo_producto
        )

        if producto is None:
            return False, "El producto no existe."

        if cantidad <= 0:
            return False, "Cantidad inválida."

        if producto.stock < cantidad:
            return False, "Stock insuficiente."

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self.ventas.append(venta)

        producto.vender(cantidad)

        return True, "Venta registrada correctamente."

    def consultar_ventas_usuario(
        self,
        identificacion: str
    ) -> list[Venta]:
        """
        Devuelve todas las ventas realizadas por un usuario.
        """

        ventas_usuario = []

        for venta in self.ventas:

            if venta.usuario_id == identificacion:
                ventas_usuario.append(venta)

        return ventas_usuario

    def listar_ventas(self):

        if not self.ventas:
            print("\nNo existen ventas registradas.\n")
            return

        print("\n========== VENTAS ==========\n")

        for venta in self.ventas:
            print(venta.mostrar_informacion())

        print()

    # =====================================
    # SET
    # =====================================

    def obtener_categorias(self) -> set[str]:
        """
        Devuelve las categorías sin repetir.
        """

        categorias = {
            producto.categoria
            for producto in self.productos
        }

        return categorias
