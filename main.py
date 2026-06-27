from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Creación del restaurante
restaurante = Restaurante("Sabores del Ecuador")

# Creación de productos
producto1 = Producto("Seco de pollo", 4.50, 10, True)
producto2 = Producto("Jugo de naranja", 1.25, 25, True)

# Creación de clientes
cliente1 = Cliente("Erick Anchundia", "0923456789", 21, True)
cliente2 = Cliente("María López", "0912345678", 30, True)

# Agregar objetos al servicio
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print(f"Restaurante: {restaurante.nombre}")
print("\nProductos registrados:")
restaurante.mostrar_productos()

print("\nClientes registrados:")
restaurante.mostrar_clientes()
