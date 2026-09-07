# Sistema de Gestión de Restaurante

## Estudiante

**Erick Steven Anchundia Martínez**

---

## Descripción general

Este proyecto es la evolución de `restaurante_app` correspondiente a la **Semana 12** de Programación Orientada a Objetos. Conserva todas las funcionalidades de la Semana 11 (registro de productos, usuarios y ventas, control de stock, persistencia JSON) e incorpora mejoras internas de rendimiento mediante el uso adecuado de colecciones.

---

## Estructura del proyecto

restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
└── main.py

---

## Mejoras de rendimiento aplicadas (Semana 12)

Las mejoras se implementaron íntegramente dentro de `servicios/restaurante.py`, sin trasladar responsabilidades a `main.py`.

### 1. Índice de productos — dict por código

Semana 11 → buscar_producto(codigo): recorre toda la lista con for — O(n)
Semana 12 → acceso directo al dict — O(1)
Semana 11 → registrar_producto (validar unicidad): llama a buscar_producto que recorre la lista
Semana 12 → comprobación `in` sobre el dict — O(1)

Colección auxiliar: _indice_productos: dict[str, Producto]
Clave: código del producto
Valor: referencia al objeto Producto

---

### 2. Índice de usuarios — dict por identificación

Semana 11 → buscar_usuario(identificacion): recorre toda la lista con for — O(n)
Semana 12 → acceso directo al dict — O(1)
Semana 11 → registrar_usuario (validar unicidad): llama a buscar_usuario que recorre la lista
Semana 12 → comprobación `in` sobre el dict — O(1)

Colección auxiliar: _indice_usuarios: dict[str, Usuario]
Clave: identificación del usuario
Valor: referencia al objeto Usuario

---

### 3. Ventas agrupadas por usuario — dict de listas

Semana 11 → consultar_ventas_usuario(id): recorre todas las ventas con for — O(n)
Semana 12 → acceso directo a la lista del usuario — O(1)

Colección auxiliar: _ventas_por_usuario: dict[str, list[Venta]]
Clave: identificación del usuario
Valor: lista de objetos Venta asociados

---

### 4. Categorías únicas — set

Semana 11 → obtener_categorias(): generaba un set recorriendo la lista en cada llamada
Semana 12 → retorna _categorias ya mantenido — O(1)

Colección auxiliar: _categorias: set[str]
Se actualiza al registrar, actualizar o eliminar productos.

---

## Sincronización y reconstrucción de índices

Al iniciar el programa: los setters de restaurante.productos, restaurante.usuarios y restaurante.ventas invocan métodos de reconstrucción (_reconstruir_indices_productos, _reconstruir_indice_usuarios, _reconstruir_ventas_por_usuario) que recrean todos los índices a partir de los objetos cargados desde JSON.

En cada operación (registrar, actualizar, eliminar, vender): los índices se actualizan de forma inmediata para mantener coherencia con las listas principales.

---

## Colecciones y su responsabilidad

_productos        → list                  → Almacenar, recorrer, listar y persistir productos
_usuarios         → list                  → Almacenar, recorrer, listar y persistir usuarios
_ventas           → list                  → Almacenar, recorrer, listar y persistir ventas
_indice_productos → dict[str, Producto]   → Búsqueda y validación de unicidad por código
_indice_usuarios  → dict[str, Usuario]    → Búsqueda y validación de unicidad por identificación
_ventas_por_usuario → dict[str, list]     → Consulta de ventas agrupadas por usuario
_categorias       → set[str]              → Categorías únicas sin recorrido adicional

---

## Ejecución

cd restaurante_app
python main.py

Requiere Python 3.10 o superior.

---

## Opciones del menú

1.  Registrar producto
2.  Buscar producto
3.  Actualizar producto
4.  Eliminar producto
5.  Listar productos
6.  Registrar usuario
7.  Listar usuarios
8.  Mostrar categorías
9.  Registrar venta
10. Listar ventas
11. Consultar ventas por usuario
12. Salir

---

## Pruebas realizadas

1. Carga inicial: se ejecuta el programa y se verifican los 9 productos, 5 usuarios y 12 ventas del JSON; los índices se reconstruyen automáticamente.
2. Buscar producto por código: se ingresa P001 y se obtiene la información sin recorrer la lista.
3. Buscar usuario por identificación: se ingresa 0901234567 y se obtiene el usuario directamente.
4. Registrar venta: se vende un producto a un usuario; el stock disminuye y la venta queda en _ventas_por_usuario.
5. Consultar ventas por usuario (opción 11): devuelve solo las ventas del usuario indicado en O(1).
6. Eliminar producto: el índice y el set de categorías quedan actualizados.
7. Reinicio: se cierra y vuelve a ejecutar el programa; los datos JSON se recuperan y los índices se reconstruyen correctamente.
