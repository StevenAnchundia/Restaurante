# Sistema de Gestión de Restaurante

## Estudiante

**Erick Steven Anchundia Martínez**

---

# Descripción

Este proyecto fue desarrollado como parte de la asignatura **Programación Orientada a Objetos**.

El sistema permite administrar productos y usuarios de un restaurante mediante un menú interactivo ejecutado desde la consola. La aplicación utiliza una arquitectura modular organizada en modelos y servicios, y cuenta con **persistencia de datos mediante archivos JSON**, garantizando que la información de los productos no se pierda al cerrar el programa. Además, aplica las principales estructuras de datos de Python para gestionar la información del sistema en memoria.

---

# Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   └── productos.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
│
└── README.md

```

---

# Descripción de los archivos

## modelos/producto.py

Contiene la clase **Producto**, encargada de representar los productos del restaurante mediante atributos como Código, Nombre, Categoría y Precio. Incorpora validaciones utilizando **@property** y **@setter**, y cuenta con el método `to_dict()` para facilitar su serialización a JSON.

## modelos/usuario.py

Contiene la clase **Usuario**, implementada mediante **@dataclass**, la cual representa la información básica de una persona registrada en el sistema.

## servicios/restaurante.py

Contiene la clase **Restaurante**, responsable de administrar las colecciones de productos y usuarios en memoria (listas). Se encarga de la lógica de negocio como registrar, buscar, actualizar, eliminar y listar.

## servicios/archivo_servicio.py

Contiene la clase **ArchivoServicio**, encargada exclusivamente de la persistencia de datos. Utiliza la librería `json` para leer y escribir la colección de objetos `Producto` en el archivo `productos.json`.

## datos/productos.json

Archivo de texto en formato JSON donde se almacenan físicamente los registros de los productos.

## main.py

Es el punto de entrada del programa. Coordina la carga inicial de datos, presenta un menú interactivo desde consola, solicita la información al usuario, utiliza los métodos de la clase `Restaurante` y sincroniza los cambios llamando a `ArchivoServicio` para guardar la información.

---

# Persistencia de Datos (Flujo de carga y guardado)

El sistema integra un flujo de persistencia transparente para el usuario:

* **Carga de datos:** Al iniciar `main.py`, se invoca el método `cargar_productos()`. Mediante `with open()` y `json.load()`, se lee el archivo `productos.json`, se validan los registros y se reconstruyen como objetos `Producto` válidos que se cargan en la memoria del restaurante.
* **Guardado de datos:** Cada vez que el usuario realiza una operación de escritura (Registrar, Actualizar o Eliminar un producto), el sistema llama automáticamente al método `guardar_productos()`. Los objetos se convierten a diccionarios y se guardan en el archivo usando `json.dump()` con codificación UTF-8, asegurando que el archivo siempre esté sincronizado con la memoria.

---

# Estructuras de datos utilizadas

* **Lista (list):** Almacena las colecciones dinámicas de productos y usuarios (`self.productos`, `self.usuarios`).
* **Tupla (tuple):** Almacena de forma inmutable las opciones del menú principal (`OPCIONES_MENU`).
* **Diccionario (dict):** Asocia cada opción del menú con la función que ejecuta la operación correspondiente (`ACCIONES`).
* **Conjunto (set):** Se utiliza para obtener y mostrar las categorías de productos evitando elementos duplicados.

---

# Manejo de Excepciones

Para garantizar la estabilidad del sistema, se controlan múltiples excepciones, especialmente durante la manipulación de archivos:

* **`FileNotFoundError`:** Si `productos.json` no existe al iniciar, el sistema lo notifica y arranca con una lista vacía sin detenerse.
* **`json.JSONDecodeError`:** Captura errores si el archivo JSON está dañado o vacío inicialmente.
* **`PermissionError`:** Avisa si no hay permisos de lectura o escritura en el directorio.
* **`KeyError` y `ValueError`:** Valida que los datos leídos del JSON estén completos y cumplan con las reglas de negocio (ej. precios mayores a cero) al reconstruir los objetos, omitiendo registros corruptos sin cerrar la aplicación.

---

# Ejecución y Pruebas

Para ejecutar el programa, asegúrese de estar en el directorio raíz del proyecto y ejecute:

```bash
python main.py

```

**Evidencia de pruebas de persistencia:**
Se comprobó satisfactoriamente la persistencia de datos cerrando y reiniciando el programa. Al agregar nuevos productos, salir de la aplicación (Opción 9) y volver a ejecutar `main.py`, el sistema recuperó con éxito toda la información guardada en `productos.json`, listando los productos previamente registrados sin ninguna pérdida de datos.


# Reflexión

Durante el desarrollo de esta actividad fue posible evolucionar un proyecto modular en Python incorporando persistencia de datos mediante archivos JSON. Se logró separar las responsabilidades creando un servicio específico para el manejo de archivos sin romper la arquitectura existente. El uso robusto del manejo de excepciones asegura que el programa sea resiliente ante errores externos, demostrando cómo construir aplicaciones más estructuradas, seguras y funcionales a largo plazo.
