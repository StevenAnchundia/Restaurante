# Sistema de Gestión de Restaurante

## Estudiante

Erick Steven Anchundia Martínez

## Descripción

Este proyecto corresponde a la Semana 7 de Programación Orientada a Objetos. El sistema permite registrar, listar y buscar productos y clientes mediante un menú interactivo en consola.

## Estructura

- modelos/
  - producto.py
  - cliente.py
- servicios/
  - restaurante.py
- main.py

## Características

- Clase `Producto` implementada con constructor `__init__`.
- Uso de `@property` y `@setter` para validar nombre, categoría y precio.
- Clase `Cliente` implementada con `@dataclass`.
- Clase `Restaurante` encargada de administrar listas de productos y clientes.
- Menú interactivo para registrar, listar y buscar información.

## Reflexión

El uso de `@property` y `@setter` permite controlar y validar los datos antes de almacenarlos en un objeto. El decorador `@dataclass` simplifica la creación de clases que contienen información, mientras que la organización modular facilita el mantenimiento y la comprensión del proyecto.
