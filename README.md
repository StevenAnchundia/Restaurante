## Sistema de Gestión de Restaurante

## Estudiante

**Erick Steven Anchundia Martínez**

---

# Descripción

Este proyecto fue desarrollado para la **Proyecto Semana 8** de la asignatura **Programación Orientada a Objetos**.

El sistema permite registrar y listar productos, bebidas y clientes mediante un menú interactivo ejecutado desde consola. El proyecto está organizado siguiendo una arquitectura modular y aplica los principios SOLID solicitados en la actividad.

---
# Estructura del proyecto
```
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
└── main.py
```

---
# Responsabilidad de cada clase

### Producto

Representa un producto general del restaurante. Contiene la información común de todos los productos, como código, nombre, categoría y precio.

### Bebida

Hereda de la clase Producto y añade el atributo específico **tamaño**, además de sobrescribir el método `mostrar_informacion()`.

### Cliente

Representa la información de un cliente registrado en el sistema.

### Restaurante

Administra las listas de productos y clientes, realizando los registros, validaciones y listados correspondientes.

### main.py

Coordina la interacción con el usuario mediante un menú interactivo, solicita los datos necesarios y utiliza la clase Restaurante para gestionar la información.

---
# Relación entre Producto y Bebida

La clase **Bebida** hereda de **Producto**, ya que una bebida es un tipo específico de producto dentro del restaurante.

Gracias a esta relación de herencia, una bebida puede reutilizar los atributos y métodos de Producto, agregando únicamente la información propia del tamaño.

---
# Principios SOLID aplicados

## S - Responsabilidad Única (SRP)

Cada clase tiene una única responsabilidad:

- Producto representa productos.
- Bebida representa bebidas.
- Cliente representa clientes.
- Restaurante administra las colecciones.
- main.py controla únicamente la interacción con el usuario.

---
## O - Abierto/Cerrado (OCP)

La incorporación de la clase Bebida amplía el sistema mediante herencia sin modificar la lógica principal de la clase Restaurante.

---

## L - Sustitución de Liskov (LSP)

Los objetos de tipo Bebida pueden almacenarse junto con los objetos Producto dentro de la misma colección y ambos responden correctamente al método `mostrar_informacion()` mediante polimorfismo.

---
# Reflexión

La aplicación de los principios SOLID permite desarrollar programas más organizados, reutilizables y fáciles de mantener. La utilización de herencia evita duplicar código, mientras que la separación de responsabilidades facilita futuras modificaciones sin afectar el funcionamiento general del sistema.
