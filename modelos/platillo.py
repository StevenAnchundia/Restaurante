from modelos.producto import Producto


class Platillo(Producto):

    def __init__(self, nombre: str, precio: float,
                 disponible: bool, calorias: int):

        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    # Polimorfismo
    def mostrar_informacion(self):

        super().mostrar_informacion()
        print(f"Calorías: {self.calorias}")
