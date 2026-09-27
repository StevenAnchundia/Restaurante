# Restaurante App

## Estudiante

**Erick Steven Anchundia Martínez**

---

# Descripción

Este proyecto corresponde a la **Semana 15** de la asignatura **Programación Orientada a Objetos**.

En esta etapa se continúa la evolución del proyecto **restaurante_app**, incorporando los **conceptos fundamentales de manejo de eventos** mediante el uso de **command=** y **callbacks** en la interfaz gráfica desarrollada con **Tkinter**.

La aplicación mantiene la arquitectura modular implementada en semanas anteriores, conservando la separación entre modelos, servicios, datos y vistas, además de la persistencia de la información mediante archivos JSON.

Como principal mejora de esta versión, se incorpora el módulo **Ventas**, permitiendo registrar una venta sencilla mediante la selección de un usuario y un producto existentes. El proceso es ejecutado mediante un botón asociado a un callback, delegando la lógica del negocio a **RestauranteServicio** y almacenando la información en **ventas.json**.

---

# Estructura del proyecto

```
restaurante_app/
│
├── assets/
│   ├── logo.png
│   ├── producto.png
│   ├── usuario.png
│   └── venta.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
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

Contiene los archivos JSON utilizados para almacenar la información de la aplicación.

- productos.json
- usuarios.json
- ventas.json

---

## modelos/

Representa las entidades principales del sistema.

### Producto

Representa cada producto disponible en el restaurante.

Contiene:

- código
- nombre
- categoría
- precio
- stock

### Usuario

Representa los usuarios registrados en el sistema.

Contiene:

- identificación
- nombre
- correo electrónico

### Venta

Representa una venta realizada dentro del restaurante.

Contiene:

- usuario
- producto
- fecha

---

## servicios/

Contiene la lógica de negocio de la aplicación.

### ArchivoServicio

Se encarga de:

- Leer archivos JSON.
- Convertir la información en objetos.
- Guardar productos.
- Guardar ventas.

### RestauranteServicio

Administra todas las operaciones del sistema.

Entre ellas:

- Validar inicio de sesión.
- Obtener productos.
- Obtener usuarios.
- Registrar productos.
- Buscar productos.
- Actualizar productos.
- Eliminar productos.
- Registrar ventas.
- Obtener ventas.

Toda la lógica del negocio permanece en esta capa, evitando que la interfaz manipule directamente los archivos JSON.

---

## ui/

Contiene todas las ventanas desarrolladas con Tkinter.

### LoginView

Permite:

- ingresar usuario
- ingresar contraseña
- validar credenciales
- acceder al sistema

### MainView

Integra toda la funcionalidad principal del restaurante.

Permite:

### Gestión de productos

- Registrar productos.
- Buscar productos.
- Actualizar productos.
- Eliminar productos.

### Consulta de usuarios

Visualiza los usuarios registrados mediante un Listbox.

### Gestión de ventas

Permite:

- seleccionar un usuario
- seleccionar un producto
- registrar una venta mediante un botón
- mostrar las ventas registradas en un Treeview

La interacción se realiza mediante **command=**, ejecutando un callback que solicita la operación al servicio correspondiente.

---

# Manejo de eventos

La aplicación implementa el fundamento principal trabajado durante la Semana 15.

```
Usuario

↓

Botón

↓

command=

↓

Callback

↓

RestauranteServicio

↓

ArchivoServicio

↓

ventas.json

↓

Actualización de la interfaz
```

De esta manera la interfaz únicamente coordina la interacción con el usuario mientras que la lógica permanece encapsulada dentro del servicio.

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

Gestión de Productos

↓

Consulta de Usuarios

↓

Registro de Venta

↓

RestauranteServicio

↓

Persistencia en ventas.json

↓

Actualización de la tabla de ventas

↓

Cerrar sesión
```

---

# Funcionalidades implementadas

✔ Inicio de sesión.

✔ Validación de usuario y contraseña.

✔ Interfaz gráfica desarrollada con Tkinter.

✔ Gestión completa de productos.

✔ Consulta de usuarios.

✔ Registro de ventas.

✔ Visualización de ventas.

✔ Persistencia mediante archivos JSON.

✔ Uso de callbacks mediante **command=**.

✔ Separación entre modelos, servicios, datos e interfaz.

✔ Arquitectura modular.

---

# Componentes utilizados

La interfaz utiliza componentes de Tkinter y ttk, entre ellos:

- Frame
- LabelFrame
- Label
- Entry
- Button
- Combobox
- Listbox
- Treeview
- Scrollbar
- MessageBox

Los componentes se organizan mediante los gestores de geometría trabajados durante la asignatura para mantener una interfaz clara y ordenada.

---

# Ejecución

Ubicarse dentro del proyecto.

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
- Tkinter (incluido en Python)
- Archivos JSON del proyecto

---

# Pruebas realizadas

Se verificó el siguiente funcionamiento:

1. Inicio correcto de la aplicación.
2. Validación del inicio de sesión.
3. Visualización de productos.
4. Visualización de usuarios.
5. Registro de productos.
6. Búsqueda de productos.
7. Actualización de productos.
8. Eliminación de productos.
9. Selección de usuario.
10. Selección de producto.
11. Registro de ventas.
12. Persistencia en ventas.json.
13. Recuperación de ventas al reiniciar la aplicación.
14. Funcionamiento correcto de los callbacks mediante command=.

---

# Tecnologías utilizadas

- Python
- Programación Orientada a Objetos
- Tkinter
- ttk
- JSON
- Git
- GitHub
