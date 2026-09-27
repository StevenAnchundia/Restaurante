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

    def obtener_usuarios(self) -> list[Usuario]:
        registros = ArchivoServicio.leer("usuarios.json")
        return [Usuario.from_dict(d) for d in registros]

    def agregar_usuario(self, nombre: str, usuario: str, contrasena: str, rol: str) -> tuple[bool, str]:
        if not nombre or not usuario or not contrasena:
            return False, "Todos los campos son obligatorios."
        usuarios = self.obtener_usuarios()
        if any(u.usuario == usuario for u in usuarios):
            return False, f"El usuario '{usuario}' ya existe."
        nuevo_id = max((u.id for u in usuarios), default=0) + 1
        nuevo = Usuario(nuevo_id, nombre, usuario, contrasena, rol)
        datos = [u.to_dict() for u in usuarios] + [nuevo.to_dict()]
        ArchivoServicio.escribir("usuarios.json", datos)
        return True, f"Usuario '{nombre}' registrado correctamente."

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
