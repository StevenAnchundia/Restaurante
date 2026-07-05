from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


restaurante = Restaurante()

# Platillos
platillo1 = Platillo("Hamburguesa", 6.50, True, 850)
platillo2 = Platillo("Pizza", 12.00, True, 1200)

# Bebidas
bebida1 = Bebida("Coca-Cola", 2.00, True, 500)
bebida2 = Bebida("Jugo de Naranja", 3.50, False, 350)

restaurante.agregar_producto(platillo1)
restaurante.agregar_producto(platillo2)
restaurante.agregar_producto(bebida1)
restaurante.agregar_producto(bebida2)

# Encapsulación
print("Precio original:", platillo1.obtener_precio())

platillo1.cambiar_precio(7.25)

print("Nuevo precio:", platillo1.obtener_precio())

print("\n")

# Polimorfismo
restaurante.mostrar_productos()
