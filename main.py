from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio

# Instancias de los servicios
restaurante = Restaurante()
archivo_servicio = ArchivoServicio("datos/productos.json")

# CARGA INICIAL: Recuperamos los datos del JSON antes de empezar
restaurante.productos = archivo_servicio.cargar_productos()

# TUPLA (Información fija)
OPCIONES_MENU = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Salir"
)

# FUNCIONES

def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE RESTAURANTE")
    print("========================================")

    for indice, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{indice}. {opcion}")
    print()


def registrar_producto():
    try:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio
        )
        if restaurante.registrar_producto(producto):
            # Guardamos los cambios en el JSON
            archivo_servicio.guardar_productos(restaurante.productos)
            print("\nProducto registrado correctamente.")
        else:
            print("\nYa existe un producto con ese código.")
    except ValueError as error:
        print(f"\nError: {error}")


def buscar_producto():
    codigo = input("Ingrese el código: ")
    producto = restaurante.buscar_producto(codigo)

    if producto:
        print("\nProducto encontrado:\n")
        print(producto.mostrar_informacion())
    else:
        print("\nProducto no encontrado.")


def actualizar_producto():
    codigo = input("Código del producto: ")
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("\nProducto no encontrado.")
        return

    try:
        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        precio = float(input("Nuevo precio: "))

        restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio
        )
        
        # Guardamos los cambios en el JSON
        archivo_servicio.guardar_productos(restaurante.productos)
        print("\nProducto actualizado correctamente.")
    except ValueError as error:
        print(error)


def eliminar_producto():
    codigo = input("Código del producto: ")
    if restaurante.eliminar_producto(codigo):
        # Guardamos los cambios en el JSON
        archivo_servicio.guardar_productos(restaurante.productos)
        print("\nProducto eliminado correctamente.")
    else:
        print("\nProducto no encontrado.")


def listar_productos():
    restaurante.listar_productos()


def registrar_usuario():
    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    usuario = Usuario(
        identificacion,
        nombre,
        correo
    )
    if restaurante.registrar_usuario(usuario):
        print("\nUsuario registrado correctamente.")
    else:
        print("\nYa existe un usuario con esa identificación.")


def listar_usuarios():
    restaurante.listar_usuarios()


def mostrar_categorias():
    categorias = restaurante.obtener_categorias()
    if not categorias:
        print("\nNo existen categorías registradas.")
        return
    print("\n===== CATEGORÍAS =====\n")
    for categoria in categorias:
        print(categoria)


# DICCIONARIO
ACCIONES = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias
}

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "9":
            print("\nGracias por utilizar el sistema.")
            break
        accion = ACCIONES.get(opcion)
        if accion:
            accion()
        else:
            print("\nOpción inválida.")


if __name__ == "__main__":
    main()
