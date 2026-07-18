from modelos import Producto, Bebida, Cliente
from servicios import Restaurante

restaurante = Restaurante()

# ==========================
#        FUNCIONES
# ==========================

def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("----------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("----------------------------------------")
    print("6. Salir")

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
            print("\n Producto registrado correctamente.")
        else:
            print("\n Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"\nError: {error}")

def registrar_bebida():
    try:
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        tamano = input("Tamaño (250 ml, 500 ml, etc.): ")

        bebida = Bebida(
            codigo,
            nombre,
            categoria,
            precio,
            tamano
        )

        if restaurante.registrar_producto(bebida):
            print("\n Bebida registrada correctamente.")
        else:
            print("\n Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"\nError: {error}")

def registrar_cliente():
    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    cliente = Cliente(
        identificacion,
        nombre,
        correo
    )

    if restaurante.registrar_cliente(cliente):
        print("\n Cliente registrado correctamente.")
    else:
        print("\n Ya existe un cliente con esa identificación.")


def listar_productos():
    restaurante.listar_productos()


def listar_clientes():
    restaurante.listar_clientes()

# ==============================
#       PROGRAMA PRINCIPAL
# ==============================

def main():

    while True:

        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            registrar_bebida()

        elif opcion == "3":
            registrar_cliente()

        elif opcion == "4":
            listar_productos()

        elif opcion == "5":
            listar_clientes()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción no válida.")

if __name__ == "__main__":
    main()

    else:

        print("Opción inválida.")

if __name__ == "__main__":
    main()
