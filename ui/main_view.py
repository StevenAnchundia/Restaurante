
import tkinter as tk
from tkinter import ttk


class MainView:

    def __init__(self, root, restaurante_servicio):

        self.root = root
        self.restaurante_servicio = restaurante_servicio

        self.on_logout = None

        self.frame = tk.Frame(root)

        self.crear_componentes()

    def crear_componentes(self):

        titulo = tk.Label(
            self.frame,
            text="SISTEMA DEL RESTAURANTE",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=10)

        # ===========================
        # PRODUCTOS
        # ===========================

        tk.Label(
            self.frame,
            text="Productos registrados",
            font=("Arial", 12, "bold")
        ).pack()

        self.lista_productos = tk.Listbox(
            self.frame,
            width=80,
            height=8
        )

        self.lista_productos.pack(pady=5)

        # ===========================
        # USUARIOS
        # ===========================

        tk.Label(
            self.frame,
            text="Usuarios registrados",
            font=("Arial", 12, "bold")
        ).pack()

        self.lista_usuarios = tk.Listbox(
            self.frame,
            width=80,
            height=6
        )

        self.lista_usuarios.pack(pady=5)

        # ===========================
        # VENTAS
        # ===========================

        tk.Label(
            self.frame,
            text="Ventas (Pendiente de implementación)",
            foreground="red"
        ).pack(pady=10)

        # ===========================
        # BOTÓN
        # ===========================

        boton = tk.Button(
            self.frame,
            text="Cerrar sesión",
            command=self.cerrar_sesion
        )

        boton.pack(pady=15)

    def mostrar(self):

        self.cargar_productos()

        self.cargar_usuarios()

        self.frame.pack(fill="both", expand=True)

    def ocultar(self):

        self.frame.pack_forget()

    # ====================================
    # PRODUCTOS
    # ====================================

    def cargar_productos(self):

        self.lista_productos.delete(0, tk.END)

        productos = self.restaurante_servicio.obtener_productos()

        for producto in productos:

            texto = (
                f"{producto.codigo} | "
                f"{producto.nombre} | "
                f"{producto.categoria} | "
                f"${producto.precio:.2f} | "
                f"Stock: {producto.stock}"
            )

            self.lista_productos.insert(
                tk.END,
                texto
            )

    # ====================================
    # USUARIOS
    # ====================================

    def cargar_usuarios(self):

        self.lista_usuarios.delete(0, tk.END)

        usuarios = self.restaurante_servicio.obtener_usuarios()

        for usuario in usuarios:

            texto = (
                f"{usuario.identificacion} | "
                f"{usuario.nombre} | "
                f"{usuario.correo}"
            )

            self.lista_usuarios.insert(
                tk.END,
                texto
            )

    # ====================================

    def cerrar_sesion(self):

        if self.on_logout:
            self.on_logout()
