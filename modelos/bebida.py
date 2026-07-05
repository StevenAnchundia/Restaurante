from modelos.producto import Producto


class Bebida(Producto):

    def __init__(self, nombre: str, precio: float,
                 disponible: bool, volumen_ml: int):

        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml

    # Polimorfismo
    def mostrar_informacion(self):

        super().mostrar_informacion()
        print(f"Volumen: {self.volumen_ml} ml")
