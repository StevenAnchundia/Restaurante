import json
from modelos import Producto


class ArchivoServicio:

    def __init__(self, ruta_archivo: str):
        self.ruta_archivo = ruta_archivo

    # CARGAR PRODUCTOS

    def cargar_productos(self) -> list[Producto]:

        productos = []

        try:

            with open(
                self.ruta_archivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                datos = json.load(archivo)

                for registro in datos:

                    try:

                        producto = Producto(
                            registro["codigo"],
                            registro["nombre"],
                            registro["categoria"],
                            registro["precio"]
                        )

                        productos.append(producto)

                    except KeyError:
                        print(
                            "Registro incompleto encontrado en el archivo."
                        )

                    except ValueError as error:
                        print(error)

        except FileNotFoundError:

            print("Archivo JSON no encontrado. Se iniciará vacío.")

        except json.JSONDecodeError:

            print("El archivo JSON está dañado.")

        except PermissionError:

            print("No existen permisos para leer el archivo.")

        return productos

    # GUARDAR PRODUCTOS
  
    def guardar_productos(
        self,
        productos: list[Producto]
    ):

        datos = [
            producto.to_dict()
            for producto in productos
        ]

        try:

            with open(
                self.ruta_archivo,
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

            print("No existen permisos para guardar el archivo.")
