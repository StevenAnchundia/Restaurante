import json
import os

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:

    def __init__(self):

        carpeta_base = os.path.dirname(
            os.path.dirname(__file__)
        )

        carpeta_datos = os.path.join(
            carpeta_base,
            "datos"
        )

        if not os.path.exists(carpeta_datos):

            os.makedirs(carpeta_datos)


        self.archivo_productos = os.path.join(
            carpeta_datos,
            "productos.json"
        )

        self.archivo_usuarios = os.path.join(
            carpeta_datos,
            "usuarios.json"
        )


    # ==========================
    # PRODUCTOS
    # ==========================

    def cargar_productos(self):

        try:

            with open(
                self.archivo_productos,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(
                    archivo
                )

            productos = []

            for producto in datos:

                productos.append(

                    Producto(
                        producto["codigo"],
                        producto["nombre"],
                        producto["categoria"],
                        producto["precio"],
                        producto["stock"]
                    )

                )

            return productos

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []

    def guardar_productos(self, productos):


        datos = []


        for producto in productos:

            datos.append(
                producto.to_dict()
            )

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


    # ==========================
    # USUARIOS
    # ==========================

    def cargar_usuarios(self):


        try:

            with open(
                self.archivo_usuarios,
                "r",
                encoding="utf-8"
            ) as archivo:


                datos = json.load(
                    archivo
                )



            usuarios = []

            for usuario in datos:

                usuarios.append(

                    Usuario(
                        usuario["identificacion"],
                        usuario["nombre"],
                        usuario["correo"]
                    )

                )

            return usuarios

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            return []
