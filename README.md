# Sistema de Gestión de Restaurante

## Estudiante

**Erick Steven Anchundia Martínez**

---

# Descripción

Este proyecto fue desarrollado como parte de la **Semana 9** de la asignatura **Programación Orientada a Objetos**.

El sistema permite administrar productos y usuarios de un restaurante mediante un menú interactivo ejecutado desde la consola. La aplicación utiliza una arquitectura modular organizada en modelos, servicios y un archivo principal, además de aplicar las principales estructuras de datos de Python para gestionar la información del sistema.

---

# Estructura del proyecto

```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
│
└── README.md
```

---

# Descripción de los archivos

## modelos/producto.py

Contiene la clase **Producto**, encargada de representar los productos del restaurante mediante atributos como:

- Código
- Nombre
- Categoría
- Precio

También incorpora validaciones utilizando **@property** y **@setter**.

---

## modelos/usuario.py

Contiene la clase **Usuario**, implementada mediante **@dataclass**, la cual representa la información básica de una persona registrada en el sistema.

Sus atributos son:

- Identificación
- Nombre
- Correo electrónico

---

## servicios/restaurante.py

Contiene la clase **Restaurante**, responsable de administrar las colecciones de productos y usuarios.

Entre sus funciones se encuentran:

- Registrar productos
- Buscar productos
- Actualizar productos
- Eliminar productos
- Listar productos
- Registrar usuarios
- Listar usuarios
- Mostrar categorías sin repetir

---

## main.py

Es el punto de entrada del programa.

Presenta un menú interactivo desde consola, solicita la información al usuario y utiliza los métodos de la clase Restaurante para realizar todas las operaciones del sistema.

---

# Estructuras de datos utilizadas

## Lista (list)

Se utiliza para almacenar las colecciones dinámicas del sistema.

```python
self.productos = []
self.usuarios = []
```

Estas listas permiten registrar, buscar, actualizar, eliminar y listar objetos durante la ejecución del programa.

---

## Tupla (tuple)

Se utiliza para almacenar las opciones del menú principal.

```python
OPCIONES_MENU = (
    "Registrar producto", "Buscar producto", "Actualizar producto", "Eliminar producto", "Listar productos", "Registrar usuario", "Listar usuarios",         "Mostrar categorías", "Salir"
)
```

Al ser información fija, la tupla garantiza que estas opciones no sean modificadas accidentalmente.

---

## Diccionario (dict)

Se utiliza para asociar cada opción del menú con la función que ejecuta la operación correspondiente.

```python
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
```

Esta estructura evita utilizar una gran cantidad de instrucciones condicionales y facilita la organización del programa.

---

## Conjunto (set)

Se utiliza para obtener las categorías de productos sin elementos repetidos.

Resultado mostrado por el sistema:

```
Comida
Bebida
Postre
```
---

# Funcionalidades del sistema

El sistema permite realizar las siguientes operaciones:

- Registrar productos.
- Buscar productos por código.
- Actualizar la información de un producto.
- Eliminar productos.
- Listar todos los productos registrados.
- Registrar usuarios.
- Listar usuarios registrados.
- Mostrar las categorías únicas de los productos.

---

# Validaciones implementadas

El sistema realiza varias validaciones para garantizar la integridad de la información.

Entre ellas:

- No permite registrar productos con códigos duplicados.
- No permite registrar usuarios con identificaciones repetidas.
- No permite nombres vacíos.
- No permite categorías vacías.
- No permite precios menores o iguales a cero.
- Utiliza manejo de excepciones para evitar errores durante el ingreso de datos.

---

# Reflexión

Durante el desarrollo de esta actividad fue posible aplicar las principales estructuras de datos de Python dentro de un proyecto modular orientado a objetos. El uso de listas permitió administrar colecciones dinámicas, la tupla almacenó información constante del sistema, el diccionario facilitó la relación entre las opciones del menú y las funciones disponibles, mientras que el conjunto permitió obtener categorías sin elementos duplicados. Esta organización mejora la claridad, reutilización y mantenimiento del código, favoreciendo el desarrollo de aplicaciones más estructuradas.
