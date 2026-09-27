import tkinter as tk
import os


class LoginView(tk.Tk):
    COLORES = {
        "fondo": "#1a1a2e",
        "panel": "#16213e",
        "acento": "#e94560",
        "texto": "#ffffff",
        "texto_suave": "#a0a0b0",
        "campo_fondo": "#0f3460",
        "boton": "#e94560",
        "boton_hover": "#c73652",
    }

    def __init__(self, servicio, al_autenticar):
        super().__init__()
        self.servicio = servicio
        self.al_autenticar = al_autenticar

        self.title("Restaurante App — Inicio de Sesión")
        self.geometry("420x560")
        self.resizable(False, False)
        self.configure(bg=self.COLORES["fondo"])

        self._construir_ui()
        self._centrar_ventana()

    def _construir_ui(self):
        # ── Logo ──
        marco_logo = tk.Frame(self, bg=self.COLORES["fondo"])
        marco_logo.pack(pady=25)

        logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                 "assets", "logo.png")
        try:
            self._img_logo = tk.PhotoImage(file=logo_path)
            tk.Label(marco_logo, image=self._img_logo,
                     bg=self.COLORES["fondo"]).pack()
        except Exception:
            tk.Label(marco_logo, text=" ", font=("Arial", 40),
                     bg=self.COLORES["fondo"],
                     fg=self.COLORES["acento"]).pack()

        tk.Label(marco_logo, text="RESTAURANTE APP",
                 font=("Arial", 16, "bold"),
                 bg=self.COLORES["fondo"],
                 fg=self.COLORES["texto"]).pack(pady=(6, 0))

        tk.Label(marco_logo, text="Sistema de Gestión de Ventas",
                 font=("Arial", 9),
                 bg=self.COLORES["fondo"],
                 fg=self.COLORES["texto_suave"]).pack()

        # ── Panel formulario ──
        panel = tk.Frame(self, bg=self.COLORES["panel"],
                         padx=30, pady=20)
        panel.pack(padx=40, pady=15, fill="x")

        # Usuario
        tk.Label(panel, text="Usuario",
                 font=("Arial", 10, "bold"),
                 bg=self.COLORES["panel"],
                 fg=self.COLORES["texto_suave"],
                 anchor="w").pack(fill="x", pady=(0, 4))

        self.entrada_usuario = tk.Entry(
            panel,
            font=("Arial", 12),
            bg=self.COLORES["campo_fondo"],
            fg=self.COLORES["texto"],
            insertbackground=self.COLORES["texto"],
            relief="flat",
            bd=5
        )
        self.entrada_usuario.pack(fill="x", ipady=6, pady=(0, 12))
        self.entrada_usuario.insert(0, "admin")

        # Contraseña
        tk.Label(panel, text="Contraseña",
                 font=("Arial", 10, "bold"),
                 bg=self.COLORES["panel"],
                 fg=self.COLORES["texto_suave"],
                 anchor="w").pack(fill="x", pady=(0, 4))

        self.entrada_contrasena = tk.Entry(
            panel,
            font=("Arial", 12),
            bg=self.COLORES["campo_fondo"],
            fg=self.COLORES["texto"],
            insertbackground=self.COLORES["texto"],
            relief="flat",
            bd=5,
            show="●"
        )
        self.entrada_contrasena.pack(fill="x", ipady=6, pady=(0, 16))
        self.entrada_contrasena.insert(0, "admin123")

        # Botón ingresar
        tk.Button(
            panel,
            text="Ingresar al sistema",
            font=("Arial", 12, "bold"),
            bg=self.COLORES["boton"],
            fg=self.COLORES["texto"],
            activebackground=self.COLORES["boton_hover"],
            activeforeground=self.COLORES["texto"],
            relief="flat",
            cursor="hand2",
            pady=8,
            command=self._callback_iniciar_sesion
        ).pack(fill="x")

        # Enter en campos
        self.entrada_usuario.bind("<Return>",
                                  lambda e: self.entrada_contrasena.focus())
        self.entrada_contrasena.bind("<Return>",
                                     lambda e: self._callback_iniciar_sesion())

        # Mensaje de error
        self.lbl_error = tk.Label(
            self, text="",
            font=("Arial", 10),
            bg=self.COLORES["fondo"],
            fg=self.COLORES["acento"]
        )
        self.lbl_error.pack(pady=(0, 4))

        # Hint
        tk.Label(self, text="Demo: admin / admin123",
                 font=("Arial", 9),
                 bg=self.COLORES["fondo"],
                 fg=self.COLORES["texto_suave"]).pack()

    def _callback_iniciar_sesion(self):
        usuario_texto = self.entrada_usuario.get().strip()
        contrasena_texto = self.entrada_contrasena.get().strip()

        if not usuario_texto or not contrasena_texto:
            self.lbl_error.config(text="⚠  Complete usuario y contraseña.")
            return

        usuario = self.servicio.autenticar(usuario_texto, contrasena_texto)

        if usuario:
            self.destroy()
            self.al_autenticar(usuario)
        else:
            self.lbl_error.config(text="⚠  Credenciales incorrectas.")
            self.entrada_contrasena.delete(0, tk.END)
            self.entrada_contrasena.focus()

    def _centrar_ventana(self):
        self.update_idletasks()
        ancho = self.winfo_width()
        alto = self.winfo_height()
        x = (self.winfo_screenwidth() - ancho) // 2
        y = (self.winfo_screenheight() - alto) // 2
        self.geometry(f"{ancho}x{alto}+{x}+{y}")
