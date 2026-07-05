# Sistema de Gestión de Restaurante

**Estudiante:** Erick Anchundia

## Descripción
Este proyecto implementa un sistema básico de gestión de restaurante en Python usando Programacion Orientada a Objetos.
## Herencia

La clase `Producto` es la clase padre.

Las clases `Platillo` y `Bebida` heredan sus atributos y métodos utilizando `super()`.

## Encapsulación

El atributo `__precio` se encuentra encapsulado y únicamente puede accederse mediante:

- obtener_precio()
- cambiar_precio()

Además, el método `cambiar_precio()` valida que el nuevo precio sea mayor que cero.

## Polimorfismo

Las clases `Platillo` y `Bebida` sobrescriben el método `mostrar_informacion()`, permitiendo que cada objeto muestre información específica al recorrer la lista de productos.

## Reflexión

Aplicar herencia permite reutilizar código y reducir duplicidad. La encapsulación protege la información importante de los objetos, mientras que el polimorfismo hace posible utilizar un mismo método con comportamientos diferentes según el tipo de objeto, logrando programas más organizados y fáciles de mantener.
