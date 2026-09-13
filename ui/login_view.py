
import tkinter as tk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, restaurante_servicio):

        self.root = root
        self.restaurante_servicio = restaurante_servicio

        self.on_login = None

        self.frame = tk.Frame(root)

        self.crear_componentes()

    def crear_componentes(self):

        titulo = tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=15)

        tk.Label(
            self.frame,
            text="Usuario"
        ).pack()

        self.entry_usuario = tk.Entry(
            self.frame,
            width=30
        )

        self.entry_usuario.pack(pady=5)

        tk.Label(
            self.frame,
            text="Contraseña"
        ).pack()

        self.entry_clave = tk.Entry(
            self.frame,
            show="*",
            width=30
        )

        self.entry_clave.pack(pady=5)

        boton = tk.Button(
            self.frame,
            text="Ingresar",
            command=self.iniciar_sesion
        )

        boton.pack(pady=20)

    def mostrar(self):

        self.frame.pack(expand=True)

    def ocultar(self):

        self.frame.pack_forget()

    def iniciar_sesion(self):

        usuario = self.entry_usuario.get()

        clave = self.entry_clave.get()

        if usuario == "" or clave == "":

            messagebox.showwarning(
                "Campos vacíos",
                "Ingrese usuario y contraseña."
            )

            return

        valido = self.restaurante_servicio.validar_login(
            usuario,
            clave
        )

        if valido:

            if self.on_login:
                self.on_login()

        else:

            messagebox.showerror(
                "Error",
                "Credenciales incorrectas."
            )
