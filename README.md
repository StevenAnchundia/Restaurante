# Restaurante App

## Estudiante

**Erick Steven Anchundia Martínez**

---

# Descripción

Este proyecto corresponde a la **Semana 16** de la asignatura **Programación Orientada a Objetos**.

Es la evolución directa de la versión de la Semana 15: se conservan el inicio de sesión, la navegación, la gestión de productos y el registro de ventas, y se amplía **únicamente la sección Usuarios** para aplicar **eventos con `bind()`** (`<<TreeviewSelect>>`, `<<ComboboxSelected>>`, `<Return>` y `<Escape>`) junto con los botones asociados mediante `command=`.

La gestión de usuarios funciona como contexto para demostrar cómo una selección, una tecla o un cambio de opción activan *callbacks* que solo coordinan la interfaz, mientras las validaciones, reglas y persistencia permanecen en `RestauranteServicio`.

---

# Estructura del proyecto

```
restaurante_app/
├── assets/
│   ├── logo.png
│   ├── ico_login.png
│   ├── ico_ventas.png
│   ├── ico_productos.png
│   ├── ico_usuarios.png
│   └── generar_assets.py
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
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

---

# Cambios de la Semana 16

## Modelo `Usuario` (`modelos/usuario.py`)

- Atributo **`rol`** con tres valores: **Administrador**, **Empleado** y **Cliente** (constantes `ROL_ADMINISTRADOR`, `ROL_EMPLEADO`, `ROL_CLIENTE`).
- `ROLES_GESTIONABLES = (Empleado, Cliente)`: roles que el administrador puede crear, editar y eliminar.
- `es_administrador()` para consultar el rol de forma sencilla.
- `normalizar_rol()` convierte los roles anteriores (`mesero`, `cajero`, `administrador`) a los nuevos, de modo que los datos de semanas previas siguen funcionando.
- El rol se persiste en `usuarios.json`.

## Servicio (`servicios/restaurante_servicio.py`)

Toda la lógica de usuarios permanece aquí; la interfaz nunca lee ni escribe JSON.

| Método | Responsabilidad |
|---|---|
| `obtener_usuarios()` | Consulta todos los usuarios. |
| `obtener_usuario_por_id(id)` | Busca el objeto `Usuario` a partir del identificador de la fila. |
| `agregar_usuario(...)` | Valida campos, rol, contraseña mínima y usuario duplicado; persiste. |
| `actualizar_usuario(...)` | Valida y actualiza; si la contraseña llega vacía, conserva la actual. |
| `eliminar_usuario(...)` | Elimina; impide borrar la cuenta autenticada o cuentas Administrador. |
| `obtener_usuarios_atencion()` | Usuarios que pueden atender ventas (no Clientes). |

Reglas de negocio aplicadas en el servicio (no en la interfaz):

- Solo el **Administrador** gestiona usuarios (`solicitante_id` verificado en cada operación).
- El administrador gestiona únicamente usuarios **Empleado** y **Cliente**.
- La cuenta con la que se inició sesión no puede eliminarse.
- No se permiten nombres de usuario duplicados.

## Interfaz (`ui/main_view.py`)

- La opción **Usuarios** del menú solo aparece para el Administrador (y `_mostrar_seccion` vuelve a validarlo).
- Formulario (nombre, usuario, contraseña, rol) y **Treeview** con ID, Nombre, Usuario y Rol.
- La tabla **no almacena información sensible**: cada fila usa el id del usuario como `iid`, y al seleccionarla se consulta el objeto mediante `RestauranteServicio`. La contraseña nunca se carga en el formulario.
- Íconos y logo se cargan desde `assets/` (menú lateral, cabecera y login).

---

# Manejo de eventos

## Eventos con `bind()`

| Evento | Widget | Callback | Qué hace |
|---|---|---|---|
| `<<TreeviewSelect>>` | Treeview | `_cb_seleccion_usuario(event)` | Obtiene el id de la fila, consulta al servicio y carga el usuario en el formulario. |
| `<<ComboboxSelected>>` | Combobox de rol | `_cb_rol_seleccionado(event)` | Actualiza la descripción del rol y el mensaje de estado. |
| `<Return>` | Campos del formulario | `_cb_tecla_return(event)` | Llama a `_cb_registrar_usuario()` (reutiliza el botón Registrar). |
| `<Escape>` | Formulario y tabla | `_cb_tecla_escape(event)` | Llama a `_cb_limpiar_usuario()` (reutiliza el botón Limpiar). |

Todos los `bind()` se agrupan en `_vincular_eventos_usuarios()`.

## Botones con `command=`

Registrar → `_cb_registrar_usuario` · Actualizar → `_cb_actualizar_usuario` · Eliminar → `_cb_eliminar_usuario` (con confirmación) · Limpiar → `_cb_limpiar_usuario`.

Se diferencian así dos mecanismos: `command=` para acciones de botón y `bind()` para eventos del teclado y de los widgets. Los atajos **no duplican lógica**: `<Return>` y `<Escape>` solo invocan los mismos métodos que usan los botones.

## Flujo

```
Selección de fila en el Treeview
        ↓
<<TreeviewSelect>>
        ↓
bind() → _cb_seleccion_usuario(event)
        ↓
id de la fila (iid)
        ↓
RestauranteServicio.obtener_usuario_por_id()
        ↓
Datos cargados en el formulario
        ↓
Actualizar / Eliminar / Limpiar (command=)
        ↓
RestauranteServicio → ArchivoServicio → usuarios.json
        ↓
Treeview actualizado + mensaje visual
```

---

# Credenciales de prueba

| Usuario | Contraseña | Rol |
|---|---|---|
| admin | admin123 | Administrador |
| mlopez | maria123 | Empleado |
| cperez | carlos123 | Empleado |
| atorres | ana123 | Empleado |
| lvera | luis123 | Cliente |

---

# Ejecución

```bash
cd restaurante_app
python main.py
```

Requisitos: Python 3.10 o superior y Tkinter (incluido en Python). Los íconos y el logo ya están en `assets/`; `generar_assets.py` es opcional.

---

# Pruebas realizadas

1. La aplicación inicia sin errores.
2. Inicio de sesión, navegación, Productos y Ventas siguen funcionando.
3. El Administrador accede a Usuarios; Empleado y Cliente no ven la opción ni pueden usar la gestión (el servicio también lo rechaza).
4. Registro de un Cliente y un Empleado; aparecen en el Treeview.
5. `<<TreeviewSelect>>` carga los datos de la fila en el formulario.
6. Actualizar conserva los cambios en `usuarios.json`.
7. Eliminar solicita confirmación previa.
8. La cuenta autenticada y las cuentas Administrador no pueden eliminarse.
9. `<Return>` registra el usuario.
10. `<Escape>` limpia el formulario y la selección.
11. `<<ComboboxSelected>>` responde al cambio de rol.
12. Al reiniciar, los usuarios se recuperan desde `usuarios.json`.

---

# Tecnologías utilizadas

Python · Programación Orientada a Objetos · Tkinter / ttk · JSON · Git · GitHub

