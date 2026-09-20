from servicios.archivo_servicio import ArchivoServicio

from modelos.producto import Producto


class RestauranteServicio:

    def __init__(self):

        self.archivo = ArchivoServicio()

        self.productos = self.archivo.cargar_productos()

        self.usuarios = self.archivo.cargar_usuarios()

    # =====================================
    # LOGIN
    # =====================================

    def validar_login(self, usuario, clave):

        if usuario == "admin" and clave == "1234":
            return True

        return False

    # =====================================
    # USUARIOS
    # =====================================

    def obtener_usuarios(self):

        return self.usuarios

    # =====================================
    # PRODUCTOS
    # =====================================

    def obtener_productos(self):

        return self.productos

    def buscar_producto(self, codigo):

        for producto in self.productos:

            if producto.codigo == codigo:

                return producto

        return None

    def registrar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):

        if self.buscar_producto(codigo):

            return False

        producto = Producto(
            codigo,
            nombre,
            categoria,
            float(precio),
            int(stock)
        )

        self.productos.append(producto)

        self.archivo.guardar_productos(
            self.productos
        )

        return True

    def actualizar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):

        producto = self.buscar_producto(codigo)

        if producto is None:

            return False

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = float(precio)
        producto.stock = int(stock)

        self.archivo.guardar_productos(
            self.productos
        )

        return True

    def eliminar_producto(self, codigo):

        producto = self.buscar_producto(codigo)

        if producto is None:

            return False

        self.productos.remove(producto)

        self.archivo.guardar_productos(
            self.productos
        )

        return True
