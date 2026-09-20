from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto

class RestauranteServicio:

    def __init__(self):

        self.archivo = ArchivoServicio()

        self.productos = self.archivo.cargar_productos()

        self.usuarios = self.archivo.cargar_usuarios()

    # ==========================
    # LOGIN
    # ==========================

    def validar_login(self, usuario, clave):

        return (
            usuario == "admin"
            and clave == "1234"
        )

    # ==========================
    # USUARIOS
    # ==========================

    def obtener_usuarios(self):

        return self.usuarios


    # ==========================
    # PRODUCTOS
    # ==========================

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

        if (
            codigo == ""
            or nombre == ""
            or categoria == ""
            or precio == ""
            or stock == ""
        ):

            raise ValueError(
                "Todos los campos son obligatorios."
            )

        if self.buscar_producto(codigo):

            return False

        try:

            precio = float(precio)

            stock = int(stock)


        except ValueError:

            raise ValueError(
                "Precio debe ser número y stock entero."
            )

        if precio <= 0:

            raise ValueError(
                "El precio debe ser mayor a cero."
            )

        if stock < 0:

            raise ValueError(
                "El stock no puede ser negativo."
            )


        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
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

        producto = self.buscar_producto(
            codigo
        )


        if producto is None:

            return False

        try:

            precio = float(precio)

            stock = int(stock)


        except ValueError:

            raise ValueError(
                "Precio inválido o stock inválido."
            )


        producto.nombre = nombre

        producto.categoria = categoria

        producto.precio = precio

        producto.stock = stock



        self.archivo.guardar_productos(
            self.productos
        )


        return True


    def eliminar_producto(self, codigo):


        producto = self.buscar_producto(
            codigo
        )


        if producto is None:

            return False



        self.productos.remove(
            producto
        )


        self.archivo.guardar_productos(
            self.productos
        )


        return True
