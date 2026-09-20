import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class LoginView:

    def __init__(self, root, servicio, mostrar_main):

        self.root = root
        self.servicio = servicio
        self.mostrar_main = mostrar_main

        self.frame = ttk.Frame(self.root, padding=30)
        self.frame.pack(fill="both", expand=True)

        titulo = ttk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=10)

        subtitulo = ttk.Label(
            self.frame,
            text="Inicio de sesión"
        )
        subtitulo.pack(pady=5)

        ttk.Label(
            self.frame,
            text="Usuario"
        ).pack(pady=(15, 0))

        self.entry_usuario = ttk.Entry(
            self.frame,
            width=30
        )
        self.entry_usuario.pack()

        ttk.Label(
            self.frame,
            text="Contraseña"
        ).pack(pady=(15, 0))

        self.entry_clave = ttk.Entry(
            self.frame,
            show="*",
            width=30
        )
        self.entry_clave.pack()

        ttk.Button(
            self.frame,
            text="Ingresar",
            command=self.ingresar
        ).pack(pady=20)

    def ingresar(self):

        usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()

        if usuario == "" or clave == "":

            messagebox.showwarning(
                "Advertencia",
                "Debe completar todos los campos."
            )

            return

        if self.servicio.validar_login(
            usuario,
            clave
        ):

            self.frame.destroy()

            self.mostrar_main()

        else:

            messagebox.showerror(
                "Error",
                "Usuario o contraseña incorrectos."
            )
