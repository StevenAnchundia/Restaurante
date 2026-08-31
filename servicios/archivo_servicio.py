import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:

    def __init__(self):

        self.carpeta = "datos"

        os.makedirs(self.carpeta, exist_ok=True)

        self.productos_archivo = os.path.join(
            self.carpeta,
            "productos.json"
        )

        self.usuarios_archivo = os.path.join(
            self.carpeta,
            "usuarios.json"
        )

        self.ventas_archivo = os.path.join(
            self.carpeta,
            "ventas.json"
        )

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def guardar_productos(self, productos):

        try:

            datos = []

            for producto in productos:
                datos.append(producto.to_dict())

            with open(
                self.productos_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print("No se pudo guardar productos.json")

    def cargar_productos(self):

        try:

            with open(
                self.productos_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                productos = []

                for p in datos:

                    producto = Producto(
                        p["codigo"],
                        p["nombre"],
                        p["categoria"],
                        p["precio"],
                        p["stock"]
                    )

                    productos.append(producto)

                return productos

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("productos.json está dañado.")
            return []

        except KeyError:
            print("Error en las claves de productos.json")
            return []

    # ==========================================
    # USUARIOS
    # ==========================================

    def guardar_usuarios(self, usuarios):

        try:

            datos = []

            for usuario in usuarios:
                datos.append(usuario.to_dict())

            with open(
                self.usuarios_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print("No fue posible guardar usuarios.")

    def cargar_usuarios(self):

        try:

            with open(
                self.usuarios_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                usuarios = []

                for u in datos:

                    usuario = Usuario(
                        u["identificacion"],
                        u["nombre"],
                        u["correo"]
                    )

                    usuarios.append(usuario)

                return usuarios

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("usuarios.json inválido.")
            return []

        except KeyError:
            print("Faltan datos en usuarios.json")
            return []

    # ==========================================
    # VENTAS
    # ==========================================

    def guardar_ventas(self, ventas):

        try:

            datos = []

            for venta in ventas:
                datos.append(venta.to_dict())

            with open(
                self.ventas_archivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

        except PermissionError:
            print("No fue posible guardar ventas.")

    def cargar_ventas(self):

        try:

            with open(
                self.ventas_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                ventas = []

                for v in datos:

                    venta = Venta(
                        v["usuario_id"],
                        v["producto_codigo"],
                        v["cantidad"]
                    )

                    ventas.append(venta)

                return ventas

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print("ventas.json inválido.")
            return []

        except KeyError:
            print("Faltan datos en ventas.json")
            return []
