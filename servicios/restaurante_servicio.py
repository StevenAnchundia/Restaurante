from modelos import Producto, Usuario, Venta
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    """Servicio central: validaciones, reglas de negocio y persistencia."""

    # ─── Autenticación ────────────────────────────────────────────────────────

    def autenticar(self, usuario: str, contrasena: str):
        """Devuelve el objeto Usuario si las credenciales son correctas, o None."""
        registros = ArchivoServicio.leer("usuarios.json")
        for datos in registros:
            u = Usuario.from_dict(datos)
            if u.usuario == usuario and u.contrasena == contrasena:
                return u
        return None

    # ─── Usuarios ─────────────────────────────────────────────────────────────

    LONGITUD_MIN_CONTRASENA = 4

    def obtener_usuarios(self) -> list[Usuario]:
        registros = ArchivoServicio.leer("usuarios.json")
        return [Usuario.from_dict(d) for d in registros]

    def obtener_usuarios_atencion(self) -> list[Usuario]:
        """Usuarios que pueden atender ventas (todos excepto Clientes)."""
        return [u for u in self.obtener_usuarios()
                if u.rol != Usuario.ROL_CLIENTE]

    def obtener_usuario_por_id(self, usuario_id: int):
        """Consulta un usuario por su identificador. Devuelve Usuario o None."""
        return next((u for u in self.obtener_usuarios() if u.id == usuario_id), None)

    def _guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        ArchivoServicio.escribir("usuarios.json", [u.to_dict() for u in usuarios])

    def _verificar_administrador(self, solicitante_id: int) -> tuple[bool, str]:
        """Regla de negocio: solo el Administrador gestiona usuarios."""
        solicitante = self.obtener_usuario_por_id(solicitante_id)
        if solicitante is None or not solicitante.es_administrador():
            return False, "Solo el Administrador puede gestionar usuarios."
        return True, ""

    def _validar_datos_usuario(self, nombre: str, usuario: str, rol: str) -> tuple[bool, str]:
        if not nombre or not usuario:
            return False, "Nombre y usuario son obligatorios."
        if rol not in Usuario.ROLES_GESTIONABLES:
            return False, ("El rol debe ser uno de: "
                           + ", ".join(Usuario.ROLES_GESTIONABLES) + ".")
        return True, ""

    def _validar_contrasena(self, contrasena: str) -> tuple[bool, str]:
        if len(contrasena) < self.LONGITUD_MIN_CONTRASENA:
            return False, (f"La contraseña debe tener al menos "
                           f"{self.LONGITUD_MIN_CONTRASENA} caracteres.")
        return True, ""

    def agregar_usuario(self, nombre: str, usuario: str, contrasena: str,
                        rol: str, solicitante_id: int) -> tuple[bool, str]:
        nombre, usuario = nombre.strip(), usuario.strip()
        ok, msg = self._verificar_administrador(solicitante_id)
        if not ok:
            return False, msg
        ok, msg = self._validar_datos_usuario(nombre, usuario, rol)
        if not ok:
            return False, msg
        ok, msg = self._validar_contrasena(contrasena)
        if not ok:
            return False, msg
        usuarios = self.obtener_usuarios()
        if any(u.usuario == usuario for u in usuarios):
            return False, f"El usuario '{usuario}' ya existe."
        nuevo_id = max((u.id for u in usuarios), default=0) + 1
        usuarios.append(Usuario(nuevo_id, nombre, usuario, contrasena, rol))
        self._guardar_usuarios(usuarios)
        return True, f"Usuario '{nombre}' registrado como {rol}."

    def actualizar_usuario(self, usuario_id: int, nombre: str, usuario: str,
                           contrasena: str, rol: str,
                           solicitante_id: int) -> tuple[bool, str]:
        """Actualiza un usuario. Si la contraseña llega vacía se conserva la actual."""
        nombre, usuario = nombre.strip(), usuario.strip()
        ok, msg = self._verificar_administrador(solicitante_id)
        if not ok:
            return False, msg
        usuarios = self.obtener_usuarios()
        objetivo = next((u for u in usuarios if u.id == usuario_id), None)
        if objetivo is None:
            return False, "Usuario no encontrado."
        if objetivo.es_administrador():
            return False, "La cuenta de Administrador no se modifica desde esta pantalla."
        ok, msg = self._validar_datos_usuario(nombre, usuario, rol)
        if not ok:
            return False, msg
        if any(u.usuario == usuario and u.id != usuario_id for u in usuarios):
            return False, f"El usuario '{usuario}' ya existe."
        if contrasena:
            ok, msg = self._validar_contrasena(contrasena)
            if not ok:
                return False, msg
            objetivo.contrasena = contrasena
        objetivo.nombre = nombre
        objetivo.usuario = usuario
        objetivo.rol = rol
        self._guardar_usuarios(usuarios)
        return True, f"Usuario '{nombre}' actualizado correctamente."

    def eliminar_usuario(self, usuario_id: int, solicitante_id: int) -> tuple[bool, str]:
        ok, msg = self._verificar_administrador(solicitante_id)
        if not ok:
            return False, msg
        if usuario_id == solicitante_id:
            return False, "No puede eliminar la cuenta con la que inició sesión."
        usuarios = self.obtener_usuarios()
        objetivo = next((u for u in usuarios if u.id == usuario_id), None)
        if objetivo is None:
            return False, "Usuario no encontrado."
        if objetivo.es_administrador():
            return False, "La cuenta de Administrador no se puede eliminar."
        self._guardar_usuarios([u for u in usuarios if u.id != usuario_id])
        return True, f"Usuario '{objetivo.nombre}' eliminado correctamente."

    # ─── Productos ────────────────────────────────────────────────────────────

    def obtener_productos(self) -> list[Producto]:
        registros = ArchivoServicio.leer("productos.json")
        return [Producto.from_dict(d) for d in registros]

    def obtener_productos_disponibles(self) -> list[Producto]:
        return [p for p in self.obtener_productos() if p.disponible]

    def agregar_producto(self, nombre: str, precio: float, categoria: str) -> tuple[bool, str]:
        if not nombre or not categoria:
            return False, "Nombre y categoría son obligatorios."
        if precio <= 0:
            return False, "El precio debe ser mayor a cero."
        productos = self.obtener_productos()
        nuevo_id = max((p.id for p in productos), default=0) + 1
        nuevo = Producto(nuevo_id, nombre, precio, categoria, True)
        datos = [p.to_dict() for p in productos] + [nuevo.to_dict()]
        ArchivoServicio.escribir("productos.json", datos)
        return True, f"Producto '{nombre}' agregado correctamente."

    def eliminar_producto(self, producto_id: int) -> tuple[bool, str]:
        productos = self.obtener_productos()
        filtrados = [p for p in productos if p.id != producto_id]
        if len(filtrados) == len(productos):
            return False, "Producto no encontrado."
        ArchivoServicio.escribir("productos.json", [p.to_dict() for p in filtrados])
        return True, "Producto eliminado correctamente."

    def toggle_disponibilidad(self, producto_id: int) -> tuple[bool, str]:
        productos = self.obtener_productos()
        for p in productos:
            if p.id == producto_id:
                p.disponible = not p.disponible
                estado = "disponible" if p.disponible else "no disponible"
                ArchivoServicio.escribir("productos.json", [x.to_dict() for x in productos])
                return True, f"'{p.nombre}' marcado como {estado}."
        return False, "Producto no encontrado."

    # ─── Ventas ───────────────────────────────────────────────────────────────

    def obtener_ventas(self) -> list[Venta]:
        registros = ArchivoServicio.leer("ventas.json")
        return [Venta.from_dict(d) for d in registros]

    def registrar_venta(self, usuario_id: int, producto_id: int, cantidad: int) -> tuple[bool, str]:
        """Valida y persiste una nueva venta. Devuelve (éxito, mensaje)."""
        # Validar cantidad
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor a cero."

        # Obtener usuario
        usuarios = self.obtener_usuarios()
        usuario = next((u for u in usuarios if u.id == usuario_id), None)
        if not usuario:
            return False, "Usuario no encontrado."

        # Obtener producto
        productos = self.obtener_productos()
        producto = next((p for p in productos if p.id == producto_id), None)
        if not producto:
            return False, "Producto no encontrado."
        if not producto.disponible:
            return False, f"El producto '{producto.nombre}' no está disponible."

        # Crear y persistir la venta
        ventas = self.obtener_ventas()
        nuevo_id = max((v.id for v in ventas), default=0) + 1
        nueva_venta = Venta(
            id=nuevo_id,
            usuario_id=usuario.id,
            usuario_nombre=usuario.nombre,
            producto_id=producto.id,
            producto_nombre=producto.nombre,
            precio_unitario=producto.precio,
            cantidad=cantidad
        )
        datos = [v.to_dict() for v in ventas] + [nueva_venta.to_dict()]
        ArchivoServicio.escribir("ventas.json", datos)
        return True, (f"Venta registrada: {producto.nombre} x{cantidad} "
                      f"= ${nueva_venta.total:.2f}")

    def resumen_ventas(self) -> dict:
        ventas = self.obtener_ventas()
        total = sum(v.total for v in ventas)
        return {
            "cantidad_ventas": len(ventas),
            "total_recaudado": round(total, 2)
        }
