# Restaurante App

## Estudiante

**Erick Steven Anchundia Martínez**

---

# Descripción

Este proyecto corresponde a la **Semana 13** de la asignatura Programación Orientada a Objetos.

En esta etapa se inicia la transición del proyecto **restaurante_app** desde una aplicación basada en consola hacia una aplicación con **interfaz gráfica utilizando Tkinter**.

La aplicación mantiene la separación entre modelos, servicios, datos y vistas gráficas, permitiendo comprender la organización de una aplicación de escritorio antes de incorporar todas las funcionalidades desarrolladas en semanas anteriores.

En esta versión se implementa una simulación de acceso mediante un Login y una ventana principal desde donde es posible visualizar la información de productos y usuarios cargados desde archivos JSON.

---

# Estructura del proyecto

```
restaurante_app/
│
├── datos/
│   ├── productos.json
│   └── usuarios.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
│
└── README.md
```

---

# Organización del proyecto

## datos/

Contiene los archivos JSON utilizados como almacenamiento local de la aplicación.

- productos.json
- usuarios.json

---

## modelos/

Representa las entidades principales del sistema.

### Producto

Representa cada producto del restaurante.

Contiene información como:

- código
- nombre
- categoría
- precio
- stock

### Usuario

Representa los usuarios utilizados para la simulación del acceso al sistema.

---

## servicios/

Contiene la lógica del sistema.

### ArchivoServicio

Es el encargado de leer los archivos JSON y convertir la información almacenada en objetos del sistema.

### RestauranteServicio

Gestiona las operaciones principales de la aplicación como:

- validar acceso
- obtener productos
- obtener usuarios
- consultar información necesaria para las vistas

Las vistas no leen directamente los archivos JSON.

---

## ui/

Contiene todas las ventanas construidas con Tkinter.

### LoginView

Es la primera ventana que visualiza el usuario.

Permite ingresar:

- usuario
- contraseña

Valida las credenciales mediante RestauranteServicio.

Si los datos son incorrectos muestra un mensaje de error.

---

### MainView

Se muestra únicamente cuando el acceso es correcto.

Permite visualizar:

- Productos registrados
- Usuarios registrados

Además presenta la opción **Ventas**, la cual queda identificada como una funcionalidad pendiente para las siguientes semanas del proyecto.

---

# Flujo de funcionamiento

```
Inicio

↓

main.py

↓

Carga de datos

↓

LoginView

↓

Validación de usuario

↓

MainView

↓

Visualizar productos

↓

Visualizar usuarios

↓

Cerrar sesión

↓

LoginView
```

---

# Funcionalidades implementadas

✔ Inicio mediante una única ventana Tkinter.

✔ Pantalla de acceso.

✔ Validación de usuario y contraseña.

✔ Mensajes para credenciales incorrectas.

✔ Cambio entre Login y ventana principal.

✔ Visualización de productos.

✔ Visualización de usuarios.

✔ Lectura de datos desde archivos JSON.

✔ Separación entre modelos, servicios y vistas.

---

# Funcionalidades pendientes

Como parte de la evolución del proyecto durante las siguientes semanas todavía no se implementan gráficamente:

- Registro de productos
- Actualización de productos
- Eliminación de productos
- Registro de usuarios
- Registro de ventas
- Control de stock desde la interfaz
- Persistencia de cambios mediante la interfaz gráfica

Estas funcionalidades se incorporarán progresivamente conforme avance la asignatura.

---

# Ejecución

Ubicarse dentro del proyecto:

```bash
cd restaurante_app
```

Ejecutar:

```bash
python main.py
```

---

# Requisitos

- Python 3.10 o superior
- Tkinter (incluido en la instalación estándar de Python)

---

# Pruebas realizadas

Se verificó el siguiente flujo de funcionamiento:

1. La aplicación inicia sin errores.
2. Se muestra la pantalla Login.
3. Los campos vacíos generan un mensaje de advertencia.
4. Las credenciales incorrectas muestran un mensaje de error.
5. Las credenciales válidas permiten ingresar al sistema.
6. La ventana principal muestra correctamente los productos cargados desde productos.json.
7. La ventana principal muestra correctamente los usuarios cargados desde usuarios.json.
8. La información es obtenida mediante RestauranteServicio.
9. La opción Cerrar sesión regresa nuevamente a la pantalla Login utilizando la misma ventana principal.

---

# Tecnologías utilizadas

- Python
- Programación Orientada a Objetos
- Tkinter
- JSON
