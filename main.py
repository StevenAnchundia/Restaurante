from modelos import Producto, Usuario
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


# ==========================================
# INSTANCIAS
# ==========================================

restaurante = Restaurante()
archivo_servicio = ArchivoServicio()


# ==========================================
# CARGA INICIAL
# ==========================================

restaurante.productos = archivo_servicio.cargar_productos()
restaurante.usuarios = archivo_servicio.cargar_usuarios()
restaurante.ventas = archivo_servicio.cargar_ventas()


# ==========================================
# TUPLA DEL MENÚ
# ==========================================

OPCIONES_MENU = (
    "Registrar producto",
    "Buscar producto",
    "Actualizar producto",
    "Eliminar producto",
    "Listar productos",
    "Registrar usuario",
    "Listar usuarios",
    "Mostrar categorías",
    "Registrar venta",
    "Listar ventas",
    "Salir"
)


# ==========================================
# MENÚ
# ==========================================

def mostrar_menu():

    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")

    for indice, opcion in enumerate(OPCIONES_MENU, start=1):
        print(f"{indice}. {opcion}")

    print()



# ==========================================
# PRODUCTOS
# ==========================================

def registrar_producto():

    try:

        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))


        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )


        if restaurante.registrar_producto(producto):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print("\nProducto registrado correctamente.")

        else:

            print("\nYa existe un producto con ese código.")


    except ValueError as error:

        print(f"\nError: {error}")



def buscar_producto():

    codigo = input("Código del producto: ")

    producto = restaurante.buscar_producto(codigo)


    if producto:

        print("\nProducto encontrado:")
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
        stock = int(input("Nuevo stock: "))


        if restaurante.actualizar_producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        ):

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            print("\nProducto actualizado correctamente.")

        else:

            print("\nNo se pudo actualizar.")


    except ValueError as error:

        print(f"\nError: {error}")



def eliminar_producto():

    codigo = input("Código del producto: ")


    if restaurante.eliminar_producto(codigo):

        archivo_servicio.guardar_productos(
            restaurante.productos
        )

        print("\nProducto eliminado correctamente.")

    else:

        print("\nProducto no encontrado.")



def listar_productos():

    restaurante.listar_productos()



# ==========================================
# USUARIOS
# ==========================================

def registrar_usuario():

    try:

        identificacion = input("Identificación: ")
        nombre = input("Nombre: ")
        correo = input("Correo: ")


        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )


        if restaurante.registrar_usuario(usuario):

            archivo_servicio.guardar_usuarios(
                restaurante.usuarios
            )

            print("\nUsuario registrado correctamente.")

        else:

            print("\nEl usuario ya existe.")


    except ValueError as error:

        print(f"\nError: {error}")



def listar_usuarios():

    restaurante.listar_usuarios()



# ==========================================
# CATEGORÍAS
# ==========================================

def mostrar_categorias():

    categorias = restaurante.obtener_categorias()


    if not categorias:

        print("\nNo existen categorías.")

        return


    print("\n========== CATEGORÍAS ==========")


    for categoria in categorias:

        print(categoria)



# ==========================================
# VENTAS
# ==========================================

def registrar_venta():

    try:

        codigo_producto = input(
            "Código del producto: "
        )

        identificacion_usuario = input(
            "Identificación del usuario: "
        )

        cantidad = int(
            input("Cantidad: ")
        )


        resultado, mensaje = restaurante.vender_producto(
            codigo_producto,
            identificacion_usuario,
            cantidad
        )


        if resultado:

            archivo_servicio.guardar_productos(
                restaurante.productos
            )

            archivo_servicio.guardar_ventas(
                restaurante.ventas
            )


        print("\n" + mensaje)


    except ValueError as error:

        print(f"\nError: {error}")



def listar_ventas():

    restaurante.listar_ventas()



# ==========================================
# DICCIONARIO DE ACCIONES
# ==========================================

ACCIONES = {

    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    "4": eliminar_producto,
    "5": listar_productos,
    "6": registrar_usuario,
    "7": listar_usuarios,
    "8": mostrar_categorias,
    "9": registrar_venta,
    "10": listar_ventas

}



# ==========================================
# MAIN
# ==========================================

def main():

    while True:

        mostrar_menu()

        opcion = input(
            "Seleccione una opción: "
        )


        if opcion == "11":

            print("\nGracias por utilizar el sistema.")
            break


        accion = ACCIONES.get(opcion)


        if accion:

            accion()

        else:

            print("\nOpción inválida.")



if __name__ == "__main__":

    main()
