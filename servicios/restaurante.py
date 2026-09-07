from modelos import Producto, Usuario, Venta


class Restaurante:

    def __init__(self):

        # ── Colecciones principales ────────────────────────────────────
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

        # dict código → Producto  (búsqueda y validación de unicidad)
        self._indice_productos: dict[str, Producto] = {}

        # dict identificación → Usuario  (búsqueda y validación de unicidad)
        self._indice_usuarios: dict[str, Usuario] = {}

        # dict identificación → [Venta, ...]  (consulta de ventas por usuario)
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

        # set de categorías únicas  (obtener_categorias sin recorrer lista)
        self._categorias: set[str] = set()

    @property
    def productos(self) -> list[Producto]:
        return self._productos

    @productos.setter
    def productos(self, lista: list[Producto]):
        """
        Permite que main.py asigne la lista cargada desde JSON
        y reconstruye todos los índices automáticamente.
        """
        self._productos = lista
        self._reconstruir_indices_productos()

    @property
    def usuarios(self) -> list[Usuario]:
        return self._usuarios

    @usuarios.setter
    def usuarios(self, lista: list[Usuario]):
        """
        Permite que main.py asigne la lista cargada desde JSON
        y reconstruye el índice de usuarios automáticamente.
        """
        self._usuarios = lista
        self._reconstruir_indice_usuarios()

    @property
    def ventas(self) -> list[Venta]:
        return self._ventas

    @ventas.setter
    def ventas(self, lista: list[Venta]):
        """
        Permite que main.py asigne la lista cargada desde JSON
        y reconstruye el índice de ventas por usuario.
        """
        self._ventas = lista
        self._reconstruir_ventas_por_usuario()

    # ── Reconstrucción de índices (llamada al cargar desde JSON) ────────

    def _reconstruir_indices_productos(self):
        """Reconstruye _indice_productos y _categorias desde la lista."""
        self._indice_productos = {
            p.codigo: p for p in self._productos
        }
        self._categorias = {
            p.categoria for p in self._productos
        }

    def _reconstruir_indice_usuarios(self):
        """Reconstruye _indice_usuarios desde la lista."""
        self._indice_usuarios = {
            u.identificacion: u for u in self._usuarios
        }

    def _reconstruir_ventas_por_usuario(self):
        """Reconstruye _ventas_por_usuario desde la lista de ventas."""
        self._ventas_por_usuario = {}
        for venta in self._ventas:
            self._ventas_por_usuario.setdefault(
                venta.usuario_id, []
            ).append(venta)

    # ── PRODUCTOS ───────────────────────────────────────────────────────

    def registrar_producto(self, producto: Producto) -> bool:
        """
        Registra un producto si el código no existe.
        Validación O(1) mediante _indice_productos.
        """
        if producto.codigo in self._indice_productos:
            return False

        self._productos.append(producto)
        self._indice_productos[producto.codigo] = producto
        self._categorias.add(producto.categoria)

        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        """
        Busca un producto por código en O(1).
        Antes: recorría toda la lista con un for.
        """
        return self._indice_productos.get(codigo)

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
        La búsqueda es O(1) gracias al índice.
        Sincroniza _categorias con el nuevo valor.
        """
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        categoria_anterior = producto.categoria

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        # Actualizar set de categorías si cambió
        if categoria_anterior != categoria:
            self._categorias.add(categoria)
            # Eliminar categoría anterior solo si ningún otro producto la usa
            if not any(
                p.categoria == categoria_anterior
                for p in self._productos
            ):
                self._categorias.discard(categoria_anterior)

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """
        Elimina un producto por código.
        Búsqueda O(1); también elimina del índice y actualiza _categorias.
        """
        producto = self._indice_productos.get(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        del self._indice_productos[codigo]

        # Eliminar la categoría del set si ya nadie la usa
        if not any(p.categoria == producto.categoria for p in self._productos):
            self._categorias.discard(producto.categoria)

        return True

    def listar_productos(self):

        if not self._productos:
            print("\nNo existen productos registrados.\n")
            return

        print("\n========== PRODUCTOS ==========\n")

        for producto in self._productos:
            print(producto.mostrar_informacion())

        print()

    # ── USUARIOS ────────────────────────────────────────────────────────

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """
        Registra un usuario si la identificación no existe.
        Validación O(1) mediante _indice_usuarios.
        """
        if usuario.identificacion in self._indice_usuarios:
            return False

        self._usuarios.append(usuario)
        self._indice_usuarios[usuario.identificacion] = usuario
        self._ventas_por_usuario.setdefault(usuario.identificacion, [])

        return True

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:
        """
        Busca un usuario por identificación en O(1).
        Antes: recorría toda la lista con un for.
        """
        return self._indice_usuarios.get(identificacion)

    def listar_usuarios(self):

        if not self._usuarios:
            print("\nNo existen usuarios registrados.\n")
            return

        print("\n========== USUARIOS ==========\n")

        for usuario in self._usuarios:
            print(usuario.mostrar_informacion())

        print()

    # ── VENTAS ──────────────────────────────────────────────────────────

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> tuple[bool, str]:
        """
        Realiza una venta.
        Ambas búsquedas son O(1) gracias a los índices.
        La venta queda registrada en _ventas y en _ventas_por_usuario.
        """
        usuario = self.buscar_usuario(identificacion_usuario)

        if usuario is None:
            return False, "El usuario no existe."

        producto = self.buscar_producto(codigo_producto)

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

        self._ventas.append(venta)

        # Sincronizar índice de ventas por usuario
        self._ventas_por_usuario.setdefault(
            usuario.identificacion, []
        ).append(venta)

        producto.vender(cantidad)

        return True, "Venta registrada correctamente."

    def consultar_ventas_usuario(
        self,
        identificacion: str
    ) -> list[Venta]:
        """
        Devuelve todas las ventas de un usuario en O(1).
        Antes: recorría toda la lista de ventas con un for.
        """
        return self._ventas_por_usuario.get(identificacion, [])

    def listar_ventas(self):

        if not self._ventas:
            print("\nNo existen ventas registradas.\n")
            return

        print("\n========== VENTAS ==========\n")

        for venta in self._ventas:
            print(venta.mostrar_informacion())

        print()

    # ── SET ─────────────────────────────────────────────────────────────

    def obtener_categorias(self) -> set[str]:
        """
        Devuelve las categorías únicas en O(1).
        Antes: generaba un set recorriendo la lista en cada llamada.
        Ahora _categorias se mantiene actualizado en cada operación.
        """
        return self._categorias

