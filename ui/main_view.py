import tkinter as tk
from tkinter import ttk, messagebox
import os


class MainView(tk.Toplevel):

    COLORES = {
        "fondo":         "#f0f4f0",     
        "sidebar":       "#2d5a45",    
        "sidebar_hover": "#3d7a5f",     
        "panel":         "#ffffff",     
        "panel_borde":   "#d4e8d4",    
        "acento":        "#4caf82",    
        "acento2":       "#ff8c61",   
        "acento3":       "#ffd166",
        "texto":         "#1a2e1a",
        "texto_suave":   "#6b8f71",
        "texto_blanco":  "#ffffff",
        "tabla_header":  "#2d5a45",
        "tabla_par":     "#f7fbf7",
        "tabla_impar":   "#ffffff",
        "boton":         "#4caf82",
        "boton_hover":   "#3d9e72",
        "boton_naranja": "#ff8c61",
        "boton_rojo":    "#e05252",
        "boton_azul":    "#5b8dd9",
        "campo_fondo":   "#f7fbf7",
        "separador":     "#c8e0c8",
    }

    ASSETS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

    def __init__(self, master, servicio, usuario_actual):
        super().__init__(master)
        self.servicio = servicio
        self.usuario_actual = usuario_actual

        self.title(f"Restaurante App — {usuario_actual.nombre}")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(bg=self.COLORES["fondo"])
        self.master.withdraw()
        self.protocol("WM_DELETE_WINDOW", self._salir)

        self._cargar_iconos()
        self._aplicar_estilos()
        self._construir_layout()
        self._centrar_ventana()
        self._mostrar_seccion("ventas")

    def _salir(self):
        self.master.destroy()

    def _centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _cargar_iconos(self):
        self._iconos = {}
        for nombre in ["logo", "ico_usuarios", "ico_productos", "ico_ventas"]:
            ruta = os.path.join(self.ASSETS, f"{nombre}.png")
            try:
                img = tk.PhotoImage(file=ruta)
                if nombre == "logo":
                    img = img.subsample(2, 2)
                self._iconos[nombre] = img
            except Exception:
                self._iconos[nombre] = None

    def _aplicar_estilos(self):
        estilo = ttk.Style(self)
        estilo.theme_use("clam")

        # Treeview
        estilo.configure("Treeview",
                         background=self.COLORES["tabla_impar"],
                         foreground=self.COLORES["texto"],
                         fieldbackground=self.COLORES["tabla_impar"],
                         rowheight=30,
                         font=("Segoe UI", 10),
                         borderwidth=0)
        estilo.configure("Treeview.Heading",
                         background=self.COLORES["tabla_header"],
                         foreground=self.COLORES["texto_blanco"],
                         font=("Segoe UI", 10, "bold"),
                         relief="flat",
                         padding=8)
        estilo.map("Treeview",
                   background=[("selected", self.COLORES["acento"])],
                   foreground=[("selected", self.COLORES["texto_blanco"])])

        # Scrollbar
        estilo.configure("TScrollbar",
                         background=self.COLORES["panel_borde"],
                         troughcolor=self.COLORES["fondo"],
                         arrowcolor=self.COLORES["texto_suave"],
                         borderwidth=0)

        # Combobox
        estilo.configure("TCombobox",
                         fieldbackground=self.COLORES["campo_fondo"],
                         foreground=self.COLORES["texto"],
                         background=self.COLORES["campo_fondo"],
                         selectbackground=self.COLORES["acento"],
                         selectforeground=self.COLORES["texto_blanco"],
                         bordercolor=self.COLORES["separador"],
                         lightcolor=self.COLORES["separador"],
                         darkcolor=self.COLORES["separador"])
        estilo.map("TCombobox",
                   fieldbackground=[("readonly", self.COLORES["campo_fondo"])],
                   foreground=[("readonly", self.COLORES["texto"])])

    # ── Layout ────────────────────────────────────────────────────────────────

    def _construir_layout(self):
        # Sidebar
        self.sidebar = tk.Frame(self, bg=self.COLORES["sidebar"], width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)
        self._construir_sidebar()

        # Área derecha
        area_derecha = tk.Frame(self, bg=self.COLORES["fondo"])
        area_derecha.pack(side="left", fill="both", expand=True)

        # Barra superior
        self.barra_top = tk.Frame(area_derecha,
                                   bg=self.COLORES["panel"],
                                   height=50)
        self.barra_top.pack(fill="x")
        self.barra_top.pack_propagate(False)

        self.lbl_seccion_top = tk.Label(
            self.barra_top,
            text="",
            font=("Segoe UI", 13, "bold"),
            bg=self.COLORES["panel"],
            fg=self.COLORES["texto"],
            padx=20)
        self.lbl_seccion_top.pack(side="left", pady=10)

        # Info usuario en barra top
        tk.Label(self.barra_top,
                 text=f"  {self.usuario_actual.nombre}  •  {self.usuario_actual.rol}",
                 font=("Segoe UI", 9),
                 bg=self.COLORES["panel"],
                 fg=self.COLORES["texto_suave"]).pack(side="right", padx=20, pady=10)

        # Línea separadora
        tk.Frame(area_derecha, bg=self.COLORES["separador"],
                 height=2).pack(fill="x")

        # Contenido principal
        self.contenido = tk.Frame(area_derecha, bg=self.COLORES["fondo"])
        self.contenido.pack(fill="both", expand=True)

        # Barra estado inferior
        self.barra_estado = tk.Label(
            area_derecha, text="",
            font=("Segoe UI", 9),
            bg=self.COLORES["panel"],
            fg=self.COLORES["texto_suave"],
            anchor="w", padx=15)
        self.barra_estado.pack(side="bottom", fill="x", ipady=4)

    def _construir_sidebar(self):
        # Cabecera sidebar
        cabecera = tk.Frame(self.sidebar, bg=self.COLORES["sidebar"])
        cabecera.pack(fill="x", pady=25, padx=15)

        if self._iconos.get("logo"):
            tk.Label(cabecera, image=self._iconos["logo"],
                     bg=self.COLORES["sidebar"]).pack()
        else:
            tk.Label(cabecera, text=" ",
                     font=("Segoe UI", 36),
                     bg=self.COLORES["sidebar"],
                     fg=self.COLORES["acento"]).pack()

        tk.Label(cabecera, text="RESTAURANTE APP",
                 font=("Segoe UI", 12, "bold"),
                 bg=self.COLORES["sidebar"],
                 fg=self.COLORES["texto_blanco"]).pack(pady=(8, 2))

        # Chip de usuario
        chip = tk.Frame(cabecera, bg=self.COLORES["acento"],
                        padx=10, pady=3)
        chip.pack(pady=4)
        tk.Label(chip, text=f"● {self.usuario_actual.rol}",
                 font=("Segoe UI", 8, "bold"),
                 bg=self.COLORES["acento"],
                 fg=self.COLORES["texto_blanco"]).pack()

        # Separador
        tk.Frame(self.sidebar, bg=self.COLORES["sidebar_hover"],
                 height=1).pack(fill="x", padx=15, pady=5)

        # Etiqueta menú
        tk.Label(self.sidebar, text="MENÚ PRINCIPAL",
                 font=("Segoe UI", 7, "bold"),
                 bg=self.COLORES["sidebar"],
                 fg=self.COLORES["texto_suave"],
                 anchor="w").pack(fill="x", padx=20, pady=(10, 5))

        # Botones navegación
        secciones = [
            (" ", "Ventas",    "ventas",    self.COLORES["acento3"]),
            (" ", "Productos", "productos", self.COLORES["acento"]),
            (" ", "Usuarios",  "usuarios",  self.COLORES["boton_azul"]),
        ]
        self._botones_nav = {}
        for emoji, etiqueta, seccion, color in secciones:
            marco_btn = tk.Frame(self.sidebar, bg=self.COLORES["sidebar"],
                                 cursor="hand2")
            marco_btn.pack(fill="x", padx=10, pady=3)

            indicador = tk.Frame(marco_btn, bg=self.COLORES["sidebar"], width=4)
            indicador.pack(side="left", fill="y")

            contenido_btn = tk.Frame(marco_btn, bg=self.COLORES["sidebar"],
                                     padx=10, pady=10)
            contenido_btn.pack(side="left", fill="x", expand=True)

            tk.Label(contenido_btn, text=f"{emoji}  {etiqueta}",
                     font=("Segoe UI", 11),
                     bg=self.COLORES["sidebar"],
                     fg=self.COLORES["texto_blanco"],
                     anchor="w").pack(fill="x")

            # Guardar referencias para resaltar
            self._botones_nav[seccion] = {
                "marco": marco_btn,
                "indicador": indicador,
                "contenido": contenido_btn,
                "color": color
            }

            # Bind click en todos los elementos del botón
            for widget in [marco_btn, indicador, contenido_btn,
                            contenido_btn.winfo_children()[0]]:
                widget.bind("<Button-1>",
                            lambda e, s=seccion: self._mostrar_seccion(s))
            # Hover
            for widget in [marco_btn, contenido_btn,
                            contenido_btn.winfo_children()[0]]:
                widget.bind("<Enter>",
                            lambda e, m=marco_btn, c=contenido_btn: self._hover_on(m, c))
                widget.bind("<Leave>",
                            lambda e, s2=seccion: self._hover_off(s2))

        # Espaciador
        tk.Frame(self.sidebar, bg=self.COLORES["sidebar"]).pack(
            fill="both", expand=True)

        # Separador
        tk.Frame(self.sidebar, bg=self.COLORES["sidebar_hover"],
                 height=1).pack(fill="x", padx=15, pady=5)

        # Botón cerrar sesión
        marco_salir = tk.Frame(self.sidebar, bg=self.COLORES["sidebar"],
                                padx=10, pady=8)
        marco_salir.pack(fill="x", pady=10)
        tk.Button(marco_salir,
                  text="⏻   Cerrar sesión",
                  font=("Segoe UI", 10),
                  bg=self.COLORES["boton_rojo"],
                  fg=self.COLORES["texto_blanco"],
                  activebackground="#c0392b",
                  activeforeground=self.COLORES["texto_blanco"],
                  relief="flat", cursor="hand2", pady=8,
                  command=self._cerrar_sesion
                  ).pack(fill="x")

    def _hover_on(self, marco, contenido):
        marco.config(bg=self.COLORES["sidebar_hover"])
        contenido.config(bg=self.COLORES["sidebar_hover"])
        for w in contenido.winfo_children():
            w.config(bg=self.COLORES["sidebar_hover"])

    def _hover_off(self, seccion):
        info = self._botones_nav[seccion]
        # No quitar hover si es la sección activa
        if getattr(self, "_seccion_activa", None) == seccion:
            return
        info["marco"].config(bg=self.COLORES["sidebar"])
        info["contenido"].config(bg=self.COLORES["sidebar"])
        for w in info["contenido"].winfo_children():
            w.config(bg=self.COLORES["sidebar"])

    def _resaltar_nav(self, activa):
        self._seccion_activa = activa
        for sec, info in self._botones_nav.items():
            if sec == activa:
                color = info["color"]
                info["marco"].config(bg=self.COLORES["sidebar_hover"])
                info["indicador"].config(bg=color)
                info["contenido"].config(bg=self.COLORES["sidebar_hover"])
                for w in info["contenido"].winfo_children():
                    w.config(bg=self.COLORES["sidebar_hover"],
                             fg=self.COLORES["texto_blanco"])
            else:
                info["marco"].config(bg=self.COLORES["sidebar"])
                info["indicador"].config(bg=self.COLORES["sidebar"])
                info["contenido"].config(bg=self.COLORES["sidebar"])
                for w in info["contenido"].winfo_children():
                    w.config(bg=self.COLORES["sidebar"],
                             fg=self.COLORES["texto_blanco"])

    # ── Navegación ────────────────────────────────────────────────────────────

    def _mostrar_seccion(self, seccion):
        for w in self.contenido.winfo_children():
            w.destroy()
        self._resaltar_nav(seccion)
        titulos = {
            "ventas": "  Registro de Ventas",
            "productos": "  Gestión de Productos",
            "usuarios": "  Usuarios del Sistema"
        }
        self.lbl_seccion_top.config(text=titulos.get(seccion, ""))
        if seccion == "ventas":
            self._construir_ventas()
        elif seccion == "productos":
            self._construir_productos()
        elif seccion == "usuarios":
            self._construir_usuarios()

    # ── Helpers UI ────────────────────────────────────────────────────────────

    def _card(self, titulo, padre=None, color_titulo=None):
        """Panel tipo tarjeta con título."""
        if padre is None:
            padre = self.contenido
        if color_titulo is None:
            color_titulo = self.COLORES["acento"]

        contenedor = tk.Frame(padre, bg=self.COLORES["fondo"])
        contenedor.pack(fill="x", padx=20, pady=(10, 0))

        # Título de la card
        tk.Label(contenedor, text=titulo,
                 font=("Segoe UI", 10, "bold"),
                 bg=self.COLORES["fondo"],
                 fg=color_titulo).pack(anchor="w", pady=(0, 4))

        # Card blanca con sombra simulada
        sombra = tk.Frame(contenedor, bg=self.COLORES["separador"])
        sombra.pack(fill="x")
        card = tk.Frame(sombra, bg=self.COLORES["panel"],
                        padx=20, pady=15)
        card.pack(fill="x", padx=1, pady=1)
        return card

    def _card_expandible(self, titulo, padre=None, color_titulo=None):
        """Card que se expande verticalmente."""
        if padre is None:
            padre = self.contenido
        if color_titulo is None:
            color_titulo = self.COLORES["acento"]

        contenedor = tk.Frame(padre, bg=self.COLORES["fondo"])
        contenedor.pack(fill="both", expand=True, padx=20, pady=(10, 15))

        tk.Label(contenedor, text=titulo,
                 font=("Segoe UI", 10, "bold"),
                 bg=self.COLORES["fondo"],
                 fg=color_titulo).pack(anchor="w", pady=(0, 4))

        sombra = tk.Frame(contenedor, bg=self.COLORES["separador"])
        sombra.pack(fill="both", expand=True)
        card = tk.Frame(sombra, bg=self.COLORES["panel"])
        card.pack(fill="both", expand=True, padx=1, pady=1)
        return card

    def _fila_campo(self, padre, etiqueta, ancho_label=16, contrasena=False):
        fila = tk.Frame(padre, bg=self.COLORES["panel"])
        fila.pack(fill="x", pady=5)
        tk.Label(fila, text=etiqueta, width=ancho_label, anchor="w",
                 bg=self.COLORES["panel"],
                 fg=self.COLORES["texto_suave"],
                 font=("Segoe UI", 10)).pack(side="left")
        show = "●" if contrasena else ""
        entrada = tk.Entry(fila, font=("Segoe UI", 10),
                           bg=self.COLORES["campo_fondo"],
                           fg=self.COLORES["texto"],
                           insertbackground=self.COLORES["texto"],
                           relief="solid", bd=1,
                           highlightthickness=1,
                           highlightcolor=self.COLORES["acento"],
                           highlightbackground=self.COLORES["separador"],
                           show=show)
        entrada.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 5))
        return entrada

    def _fila_combo(self, padre, etiqueta, valores, ancho_label=16):
        fila = tk.Frame(padre, bg=self.COLORES["panel"])
        fila.pack(fill="x", pady=5)
        tk.Label(fila, text=etiqueta, width=ancho_label, anchor="w",
                 bg=self.COLORES["panel"],
                 fg=self.COLORES["texto_suave"],
                 font=("Segoe UI", 10)).pack(side="left")
        combo = ttk.Combobox(fila, values=valores,
                             state="readonly", font=("Segoe UI", 10))
        if valores:
            combo.current(0)
        combo.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 5))
        return combo

    def _boton_accion(self, padre, texto, color, comando, ancho=None):
        kwargs = dict(
            text=texto,
            font=("Segoe UI", 10, "bold"),
            bg=color, fg=self.COLORES["texto_blanco"],
            activebackground=color,
            activeforeground=self.COLORES["texto_blanco"],
            relief="flat", cursor="hand2", pady=8,
            command=comando)
        if ancho:
            kwargs["width"] = ancho
        return tk.Button(padre, **kwargs)

    def _treeview(self, padre, columnas, anchos):
        marco = tk.Frame(padre, bg=self.COLORES["panel"])
        marco.pack(fill="both", expand=True, padx=15, pady=(10, 10))

        tree = ttk.Treeview(marco, columns=columnas,
                             show="headings", selectmode="browse")
        for col, ancho in zip(columnas, anchos):
            tree.heading(col, text=col)
            tree.column(col, width=ancho, minwidth=30, anchor="center")

        tree.tag_configure("par", background=self.COLORES["tabla_par"])
        tree.tag_configure("impar", background=self.COLORES["tabla_impar"])

        sb = ttk.Scrollbar(marco, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=sb.set)
        tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        return tree

    def _limpiar(self, tree):
        for i in tree.get_children():
            tree.delete(i)

    def _estado(self, texto, color=None):
        if color is None:
            color = self.COLORES["acento"]
        self.barra_estado.config(text=f"  ✓  {texto}", fg=color)
        self.after(5000, lambda: self.barra_estado.config(text=""))

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN VENTAS
    # ═════════════════════════════════════════════════════════════════════════

    def _construir_ventas(self):
        area = tk.Frame(self.contenido, bg=self.COLORES["fondo"])
        area.pack(fill="both", expand=True)

        # ── Formulario ──
        form = self._card("  Nueva venta", area,
                          color_titulo=self.COLORES["acento"])

        usuarios = self.servicio.obtener_usuarios()
        opts_u = [f"{u.id} — {u.nombre} ({u.rol})" for u in usuarios]
        self.combo_usuario_v = self._fila_combo(
            form, "Atendido por:", opts_u)

        prods = self.servicio.obtener_productos_disponibles()
        opts_p = [f"{p.id} — {p.nombre}  (${p.precio:.2f})" for p in prods]
        self.combo_producto_v = self._fila_combo(
            form, "Producto:", opts_p)

        # Cantidad + botón en la misma fila
        fila_bot = tk.Frame(form, bg=self.COLORES["panel"])
        fila_bot.pack(fill="x", pady=(10, 0))

        tk.Label(fila_bot, text="Cantidad:", width=16, anchor="w",
                 bg=self.COLORES["panel"],
                 fg=self.COLORES["texto_suave"],
                 font=("Segoe UI", 10)).pack(side="left")

        self.spin_cantidad = tk.Spinbox(
            fila_bot, from_=1, to=50, width=6,
            font=("Segoe UI", 11),
            bg=self.COLORES["campo_fondo"],
            fg=self.COLORES["texto"],
            buttonbackground=self.COLORES["separador"],
            relief="solid", bd=1)
        self.spin_cantidad.pack(side="left", ipady=5, padx=(0, 20))

        self._boton_accion(
            fila_bot, "  Registrar venta",
            self.COLORES["acento"],
            self._callback_registrar_venta
        ).pack(side="left", fill="x", expand=True, padx=(0, 5))

        # Mensaje resultado
        self.lbl_resultado_v = tk.Label(
            form, text="", font=("Segoe UI", 9, "bold"),
            bg=self.COLORES["panel"],
            fg=self.COLORES["acento"])
        self.lbl_resultado_v.pack(anchor="w", pady=(6, 0))

        # ── Tabla ventas ──
        tabla_card = self._card_expandible(
            "  Historial de ventas", area,
            color_titulo=self.COLORES["texto_suave"])

        cols = ("ID", "Usuario", "Producto", "Cant.", "Total", "Fecha")
        anchos = (45, 155, 195, 55, 85, 155)
        self.tree_ventas = self._treeview(tabla_card, cols, anchos)

        self.lbl_resumen_v = tk.Label(
            tabla_card, text="",
            font=("Segoe UI", 9, "bold"),
            bg=self.COLORES["panel"],
            fg=self.COLORES["acento2"])
        self.lbl_resumen_v.pack(pady=(0, 8))

        self._poblar_ventas()

    def _callback_registrar_venta(self):
        sel_u = self.combo_usuario_v.get()
        sel_p = self.combo_producto_v.get()
        cant = self.spin_cantidad.get()

        if not sel_u or not sel_p:
            self._msg_venta("⚠  Seleccione usuario y producto.", error=True)
            return
        try:
            uid = int(sel_u.split("—")[0].strip())
            pid = int(sel_p.split("—")[0].strip())
            cantidad = int(cant)
        except (ValueError, IndexError):
            self._msg_venta("⚠  Selección inválida.", error=True)
            return

        exito, mensaje = self.servicio.registrar_venta(uid, pid, cantidad)
        if exito:
            self._poblar_ventas()
            self.spin_cantidad.delete(0, tk.END)
            self.spin_cantidad.insert(0, "1")
            self._msg_venta(f"✓  {mensaje}", error=False)
            self._estado(mensaje)
        else:
            self._msg_venta(f"⚠  {mensaje}", error=True)

    def _msg_venta(self, texto, error=False):
        color = self.COLORES["boton_rojo"] if error else self.COLORES["acento"]
        self.lbl_resultado_v.config(text=texto, fg=color)
        self.after(4000, lambda: self.lbl_resultado_v.config(text=""))

    def _poblar_ventas(self):
        self._limpiar(self.tree_ventas)
        for i, v in enumerate(reversed(self.servicio.obtener_ventas())):
            tag = "par" if i % 2 == 0 else "impar"
            self.tree_ventas.insert("", "end",
                                    values=(v.id, v.usuario_nombre,
                                            v.producto_nombre, v.cantidad,
                                            f"${v.total:.2f}", v.fecha),
                                    tags=(tag,))
        r = self.servicio.resumen_ventas()
        self.lbl_resumen_v.config(
            text=f"Total de ventas: {r['cantidad_ventas']}   •   "
                 f"Recaudado: ${r['total_recaudado']:.2f}")

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN PRODUCTOS
    # ═════════════════════════════════════════════════════════════════════════

    def _construir_productos(self):
        area = tk.Frame(self.contenido, bg=self.COLORES["fondo"])
        area.pack(fill="both", expand=True)

        form = self._card("  Agregar producto", area,
                          color_titulo=self.COLORES["acento"])

        self.e_nombre_p = self._fila_campo(form, "Nombre:")
        self.e_precio_p = self._fila_campo(form, "Precio (USD):")
        self.combo_cat = self._fila_combo(
            form, "Categoría:",
            ["Plato fuerte", "Entrada", "Bebida", "Postre", "Especial"])

        fila_btn = tk.Frame(form, bg=self.COLORES["panel"])
        fila_btn.pack(fill="x", pady=(10, 0))
        self._boton_accion(fila_btn, "  Agregar",
                           self.COLORES["acento"],
                           self._cb_agregar_producto).pack(side="left", padx=(0, 8))

        tabla_card = self._card_expandible(
            "  Menú del restaurante", area,
            color_titulo=self.COLORES["texto_suave"])

        cols = ("ID", "Nombre", "Precio", "Categoría", "Disponible")
        self.tree_prod = self._treeview(tabla_card, cols, (45, 230, 85, 130, 85))

        fila_acc = tk.Frame(tabla_card, bg=self.COLORES["panel"])
        fila_acc.pack(pady=(0, 10))
        self._boton_accion(fila_acc, "⇄  Cambiar disponibilidad",
                           self.COLORES["boton_azul"],
                           self._cb_toggle_disp).pack(side="left", padx=(15, 8))
        self._boton_accion(fila_acc, "🗑  Eliminar",
                           self.COLORES["boton_rojo"],
                           self._cb_eliminar_prod).pack(side="left")

        self._poblar_productos()

    def _cb_agregar_producto(self):
        nombre = self.e_nombre_p.get().strip()
        precio_txt = self.e_precio_p.get().strip()
        categoria = self.combo_cat.get()
        try:
            precio = float(precio_txt)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número.", parent=self)
            return
        exito, msg = self.servicio.agregar_producto(nombre, precio, categoria)
        if exito:
            self.e_nombre_p.delete(0, tk.END)
            self.e_precio_p.delete(0, tk.END)
            self._poblar_productos()
            self._estado(msg)
        else:
            messagebox.showerror("Error", msg, parent=self)

    def _cb_toggle_disp(self):
        sel = self.tree_prod.selection()
        if not sel:
            messagebox.showwarning("Aviso", "Seleccione un producto.", parent=self)
            return
        pid = int(self.tree_prod.item(sel[0])["values"][0])
        exito, msg = self.servicio.toggle_disponibilidad(pid)
        if exito:
            self._poblar_productos()
            self._estado(msg)

    def _cb_eliminar_prod(self):
        sel = self.tree_prod.selection()
        if not sel:
            messagebox.showwarning("Aviso", "Seleccione un producto.", parent=self)
            return
        vals = self.tree_prod.item(sel[0])["values"]
        if messagebox.askyesno("Confirmar", f"¿Eliminar '{vals[1]}'?", parent=self):
            exito, msg = self.servicio.eliminar_producto(int(vals[0]))
            if exito:
                self._poblar_productos()
                self._estado(msg, self.COLORES["boton_rojo"])

    def _poblar_productos(self):
        self._limpiar(self.tree_prod)
        for i, p in enumerate(self.servicio.obtener_productos()):
            tag = "par" if i % 2 == 0 else "impar"
            self.tree_prod.insert("", "end",
                                  values=(p.id, p.nombre,
                                          f"${p.precio:.2f}",
                                          p.categoria,
                                          "✓  Sí" if p.disponible else "✗  No"),
                                  tags=(tag,))

    # ═════════════════════════════════════════════════════════════════════════
    # SECCIÓN USUARIOS
    # ═════════════════════════════════════════════════════════════════════════

    def _construir_usuarios(self):
        area = tk.Frame(self.contenido, bg=self.COLORES["fondo"])
        area.pack(fill="both", expand=True)

        form = self._card("  Registrar usuario", area,
                          color_titulo=self.COLORES["acento"])

        self.e_nombre_u = self._fila_campo(form, "Nombre completo:")
        self.e_usuario_u = self._fila_campo(form, "Nombre de usuario:")
        self.e_contra_u = self._fila_campo(form, "Contraseña:", contrasena=True)
        self.combo_rol = self._fila_combo(
            form, "Rol:", ["mesero", "cajero", "administrador"])

        fila_btn = tk.Frame(form, bg=self.COLORES["panel"])
        fila_btn.pack(fill="x", pady=(10, 0))
        self._boton_accion(fila_btn, "  Agregar usuario",
                           self.COLORES["acento"],
                           self._cb_agregar_usuario).pack(side="left")

        tabla_card = self._card_expandible(
            "  Usuarios registrados", area,
            color_titulo=self.COLORES["texto_suave"])

        cols = ("ID", "Nombre", "Usuario", "Rol")
        self.tree_usu = self._treeview(tabla_card, cols, (45, 220, 160, 130))
        self._poblar_usuarios()

    def _cb_agregar_usuario(self):
        nombre = self.e_nombre_u.get().strip()
        usuario = self.e_usuario_u.get().strip()
        contra = self.e_contra_u.get().strip()
        rol = self.combo_rol.get()
        exito, msg = self.servicio.agregar_usuario(nombre, usuario, contra, rol)
        if exito:
            for e in [self.e_nombre_u, self.e_usuario_u, self.e_contra_u]:
                e.delete(0, tk.END)
            self._poblar_usuarios()
            self._estado(msg)
        else:
            messagebox.showerror("Error", msg, parent=self)

    def _poblar_usuarios(self):
        self._limpiar(self.tree_usu)
        for i, u in enumerate(self.servicio.obtener_usuarios()):
            tag = "par" if i % 2 == 0 else "impar"
            self.tree_usu.insert("", "end",
                                 values=(u.id, u.nombre, u.usuario, u.rol),
                                 tags=(tag,))

    # ── Cerrar sesión ─────────────────────────────────────────────────────────

    def _cerrar_sesion(self):
        if messagebox.askyesno("Cerrar sesión",
                               "¿Desea cerrar sesión?", parent=self):
            self.master.destroy()
