# 🍽 restaurante_app

Sistema de Gestión de Ventas para Restaurante  
**Asignatura:** Programación Orientada a Objetos  
**Semana 15:** Conceptos fundamentales de manejo de eventos

---

## Descripción

`restaurante_app` es una aplicación de escritorio desarrollada con **Python** y **Tkinter/ttk** que permite gestionar usuarios, productos del menú y ventas de un restaurante. La persistencia se realiza mediante archivos **JSON**, y la arquitectura sigue una separación clara de responsabilidades (modelos, servicios, interfaz).

---

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json       ← Menú del restaurante
│   ├── usuarios.json        ← Personal del sistema
│   └── ventas.json          ← Historial de ventas (Semana 15)
├── modelos/
│   ├── __init__.py
│   ├── producto.py          ← Modelo Producto
│   ├── usuario.py           ← Modelo Usuario
│   └── venta.py             ← Modelo Venta (Semana 15)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py  ← Capa de acceso a datos JSON
│   └── restaurante_servicio.py ← Lógica de negocio y validaciones
├── ui/
│   ├── __init__.py
│   ├── login_view.py        ← Pantalla de inicio de sesión
│   └── main_view.py         ← Ventana principal (Usuarios, Productos, Ventas)
├── assets/                  ← Íconos PNG y logo del sistema
│   ├── logo.png
│   ├── ico_usuarios.png
│   ├── ico_productos.png
│   ├── ico_ventas.png
│   └── ico_login.png
├── main.py                  ← Punto de entrada
└── README.md
```

---

## Requisitos

- Python 3.10 o superior
- Pillow (para generación de íconos):  
  ```bash
  pip install pillow
  ```
- Tkinter (incluido en la instalación estándar de Python)

---

## Instalación y ejecución

```bash
# 1. Clonar o descomprimir el proyecto
# 2. (Opcional) Regenerar los íconos si no existen
python assets/generar_assets.py

# 3. Iniciar la aplicación
python main.py
```

**Credenciales de demo:**

| Usuario  | Contraseña | Rol            |
|----------|------------|----------------|
| admin    | admin123   | administrador  |
| mlopez   | maria123   | mesero         |
| cperez   | carlos123  | mesero         |
| atorres  | ana123     | cajero         |

---

## Funcionalidades

###  Inicio de sesión
- Validación de credenciales mediante `RestauranteServicio`
- Interfaz estilizada con logo y respuesta visual de errores

###  Usuarios
- Consulta de usuarios registrados en tabla Treeview
- Registro de nuevos usuarios con rol asignado
- Persistencia automática en `usuarios.json`

###  Productos
- Gestión completa del menú: agregar, eliminar, cambiar disponibilidad
- Filtrado de productos disponibles para la sección de ventas
- Persistencia en `productos.json`

###  Ventas *(nuevo — Semana 15)*
- Selección de usuario atendedor y producto del menú
- Campo de cantidad con control Spinbox
- Botón **Registrar venta** conectado mediante `command=` al callback `_callback_registrar_venta`
- El callback delega la operación a `RestauranteServicio.registrar_venta()`
- Persistencia inmediata en `ventas.json`
- Actualización automática del Treeview de historial
- Resumen de totales recaudados
- Respuesta visual al usuario (mensaje de éxito/error)

---

## Flujo de manejo de eventos (Semana 15)

```
USUARIO
   ↓
presiona "Registrar venta"
   ↓
BOTÓN (command=_callback_registrar_venta)
   ↓
CALLBACK: obtiene selecciones de la interfaz
   ↓
RestauranteServicio.registrar_venta(usuario_id, producto_id, cantidad)
   ↓
Validaciones (usuario existe, producto disponible, cantidad > 0)
   ↓
ArchivoServicio.escribir("ventas.json", ...)  ← PERSISTENCIA
   ↓
RESPUESTA VISUAL: actualización del Treeview + mensaje de resultado
```

---

## Evolución del proyecto

| Semana | Incorporaciones principales |
|--------|-----------------------------|
| 10–12  | Modelos base, servicios, LoginView |
| 13–14  | Secciones Usuarios y Productos, Treeview, gestión del menú |
| **15** | **Modelo Venta, ventas.json, sección Ventas, manejo de eventos con command= y callback, assets obligatorios** |

---

## Notas técnicas

- La lógica de negocio (validaciones, reglas) reside **únicamente** en `RestauranteServicio`.
- La interfaz (`main_view.py`) **no** manipula directamente los archivos JSON.
- Los callbacks obtienen datos de los componentes de la UI y los pasan al servicio.
- Los íconos se generan con Pillow mediante `assets/generar_assets.py`.
