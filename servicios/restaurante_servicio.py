from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """
    Servicio encargado de trabajar con los productos
    y usuarios del restaurante.
    """

    def __init__(self):

        self.archivo_servicio = ArchivoServicio()

        self.productos = self.archivo_servicio.cargar_productos()
        self.usuarios = self.archivo_servicio.cargar_usuarios()

    # ======================================
    # LOGIN
    # ======================================

    def validar_login(self, usuario: str, clave: str) -> bool:
        """
        Simulación de acceso al sistema.
        """

        return usuario == "admin" and clave == "1234"

    # ======================================
    # PRODUCTOS
    # ======================================

    def obtener_productos(self) -> list[Producto]:
        """
        Devuelve la lista de productos.
        """

        return self.productos

    # ======================================
    # USUARIOS
    # ======================================

    def obtener_usuarios(self) -> list[Usuario]:
        """
        Devuelve la lista de usuarios.
        """

        return self.usuarios
