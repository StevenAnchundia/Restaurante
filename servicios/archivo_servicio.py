import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:

    def __init__(self):

        carpeta_base = os.path.dirname(os.path.dirname(__file__))
        carpeta_datos = os.path.join(carpeta_base, "datos")

        self.archivo_productos = os.path.join(
            carpeta_datos,
            "productos.json"
        )

        self.archivo_usuarios = os.path.join(
            carpeta_datos,
            "usuarios.json"
        )

    # =====================================
    # PRODUCTOS
    # =====================================

    def cargar_productos(self):

        try:

            with open(
                self.archivo_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            productos = []

            for p in datos:

                productos.append(

                    Producto(
                        p["codigo"],
                        p["nombre"],
                        p["categoria"],
                        p["precio"],
                        p["stock"]
                    )

                )

            return productos

        except FileNotFoundError:

            return []

    def guardar_productos(self, productos):

        datos = []

        for producto in productos:

            datos.append(producto.to_dict())

        with open(
            self.archivo_productos,
            "w",
            encoding="utf-8"
        ) as archivo:

            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

    # =====================================
    # USUARIOS
    # =====================================

    def cargar_usuarios(self):

        try:

            with open(
                self.archivo_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

            usuarios = []

            for u in datos:

                usuarios.append(

                    Usuario(
                        u["identificacion"],
                        u["nombre"],
                        u["correo"]
                    )

                )

            return usuarios

        except FileNotFoundError:

            return []
