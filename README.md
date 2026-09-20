# Restaurante App

## Estudiante

**Erick Steven Anchundia Martínez**

---

# Descripción

Este proyecto corresponde a la **Semana 14** de la asignatura Programación Orientada a Objetos.

En esta etapa se continúa la evolución del proyecto **restaurante_app**, incorporando mejoras en la interfaz gráfica mediante el uso de **componentes, contenedores y gestores de geometría de Tkinter**.

La aplicación mantiene la separación entre modelos, servicios, datos y vistas gráficas, permitiendo una mejor organización del sistema y evitando concentrar la lógica del negocio dentro de la interfaz.

En esta versión se implementa una interfaz principal para la gestión de productos, permitiendo registrar, consultar, actualizar y eliminar productos mediante componentes gráficos, manteniendo la persistencia de información mediante archivos JSON.

---

# Estructura del proyecto


restaurante_app/
│
├── datos/
│ ├── productos.json
│ └── usuarios.json
│
├── modelos/
│ ├── init.py
│ ├── producto.py
│ └── usuario.py
│
├── servicios/
│ ├── init.py
│ ├── archivo_servicio.py
│ └── restaurante_servicio.py
│
├── ui/
│ ├── init.py
│ ├── login_view.py
│ └── main_view.py
│
├── main.py
│
└── README.md


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

Representa los usuarios registrados dentro del sistema.

---

## servicios/

Contiene la lógica del sistema y las operaciones principales.

### ArchivoServicio

Es el encargado de leer y escribir los archivos JSON, realizando la conversión entre información almacenada y objetos utilizados por la aplicación.

### RestauranteServicio

Gestiona las operaciones principales del sistema como:

- validar acceso
- obtener productos
- obtener usuarios
- registrar productos
- consultar productos
- actualizar productos
- eliminar productos

Las vistas no realizan lectura ni escritura directa sobre los archivos JSON, manteniendo la separación de responsabilidades.

---

## ui/

Contiene las ventanas construidas mediante Tkinter.

### LoginView

Es la primera ventana visualizada por el usuario.

Permite ingresar:

- usuario
- contraseña

La validación de acceso se realiza mediante RestauranteServicio.

Si las credenciales son correctas permite ingresar a la ventana principal del sistema.

---

### MainView

Es la ventana principal de la aplicación.

Utiliza componentes y contenedores de Tkinter para organizar la interfaz gráfica.

Permite:

- Registrar productos.
- Consultar productos mediante código.
- Actualizar información de productos.
- Eliminar productos.
- Visualizar productos registrados mediante una tabla.
- Consultar usuarios registrados.

Las operaciones realizadas desde la interfaz son procesadas mediante RestauranteServicio.

---

# Componentes y contenedores utilizados

Para la construcción de la interfaz gráfica se utilizaron componentes de Tkinter y ttk:

- Frame: utilizado para organizar las diferentes zonas de la aplicación.
- LabelFrame: utilizado para separar visualmente las secciones del sistema.
- Label: utilizado para mostrar información.
- Entry: utilizado para capturar datos de productos.
- Button: utilizado para ejecutar acciones mediante el parámetro command=.
- Treeview: utilizado para mostrar productos en forma de tabla.
- Scrollbar: utilizado para facilitar la navegación dentro de la tabla.
- Listbox: utilizado para mostrar usuarios registrados.

Los gestores de geometría utilizados fueron:

- pack()
- grid()

Estos permiten distribuir correctamente los componentes dentro de los contenedores y mejorar la organización visual de la aplicación.

---

# Flujo de funcionamiento


Inicio

↓

main.py

↓

Carga de servicios y datos JSON

↓

LoginView

↓

Validación mediante RestauranteServicio

↓

MainView

↓

Gestión de productos y consulta de usuarios

↓

Operaciones CRUD

↓

Actualización de productos.json

↓

Actualización de información mostrada


---

# Funcionalidades implementadas

✔ Inicio mediante interfaz gráfica Tkinter.

✔ Pantalla de acceso mediante LoginView.

✔ Validación de usuario y contraseña.

✔ Separación entre modelos, servicios, datos e interfaz.

✔ Organización visual mediante componentes y contenedores.

✔ Registro de productos.

✔ Consulta de productos mediante código.

✔ Actualización de productos existentes.

✔ Eliminación de productos.

✔ Visualización de productos mediante Treeview.

✔ Consulta de usuarios registrados.

✔ Uso de botones mediante command=.

✔ Persistencia de información mediante productos.json.

✔ Actualización automática de la información mostrada después de cada operación.

---

# Funcionalidades pendientes

Como parte de futuras mejoras del proyecto se pueden incorporar:

- Gestión completa de ventas.
- Control avanzado de inventario.
- Nuevas mejoras visuales.
- Nuevos módulos administrativos.

---

# Persistencia de información

La información del sistema se mantiene mediante archivos JSON:


datos/productos.json
datos/usuarios.json


La lectura y escritura de archivos se realiza únicamente mediante ArchivoServicio, evitando manipular directamente los archivos desde la interfaz gráfica.

---

# Ejecución

Ubicarse dentro del proyecto:

```bash
cd restaurante_app

Ejecutar:

python main.py

Credenciales de acceso:

Usuario:

admin

Contraseña:

1234
Pruebas realizadas

Se verificó el siguiente funcionamiento:

La aplicación inicia correctamente desde main.py.
El Login permite validar credenciales.
Los campos vacíos muestran mensajes de advertencia.
Las credenciales incorrectas muestran mensajes de error.
El acceso correcto permite ingresar a MainView.
La interfaz muestra correctamente los productos cargados desde productos.json.
La interfaz muestra correctamente los usuarios registrados desde usuarios.json.
Se puede registrar un nuevo producto.
Se puede consultar un producto mediante su código.
Se puede actualizar la información de un producto.
Se puede eliminar un producto.
Los cambios realizados se guardan correctamente en productos.json.
Después de reiniciar la aplicación, la información permanece disponible.
La interfaz solicita las operaciones mediante RestauranteServicio sin manipular directamente los archivos JSON.
Tecnologías utilizadas
Python
Programación Orientada a Objetos
Tkinter / ttk
Archivos JSON
GitHub
