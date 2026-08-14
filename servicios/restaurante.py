from modelos import Producto, Usuario


class Restaurante:
    """
    Clase encargada de administrar los productos y usuarios del sistema.
    """

    def __init__(self):
        # Listas (list)
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

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
        Busca un producto por su código.
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
        precio: float
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

        for usuario_existente in self.usuarios:

            if (
                usuario_existente.identificacion
                == usuario.identificacion
            ):
                return False

        self.usuarios.append(usuario)

        return True

    def listar_usuarios(self):

        if not self.usuarios:
            print("\nNo existen usuarios registrados.\n")
            return

        print("\n========== USUARIOS ==========\n")

        for usuario in self.usuarios:
            print(usuario.mostrar_informacion())

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
    
