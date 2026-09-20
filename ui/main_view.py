import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainView:

    def __init__(self, root, servicio, cerrar_sesion):

        self.root = root
        self.servicio = servicio
        self.cerrar_sesion = cerrar_sesion

        self.frame = ttk.Frame(root, padding=15)
        self.frame.pack(fill="both", expand=True)

        titulo = ttk.Label(
            self.frame,
            text="SISTEMA DEL RESTAURANTE",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=10)

        # ==========================
        # CONTENEDOR PRINCIPAL
        # ==========================

        contenedor = ttk.Frame(self.frame)
        contenedor.pack(fill="both", expand=True)

        # --------------------------
        # IZQUIERDA
        # --------------------------

        izquierda = ttk.LabelFrame(
            contenedor,
            text="Gestión de Productos",
            padding=10
        )

        izquierda.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="n"
        )

        ttk.Label(izquierda,text="Código").grid(row=0,column=0,sticky="w")
        self.codigo=ttk.Entry(izquierda,width=25)
        self.codigo.grid(row=0,column=1,pady=3)

        ttk.Label(izquierda,text="Nombre").grid(row=1,column=0,sticky="w")
        self.nombre=ttk.Entry(izquierda,width=25)
        self.nombre.grid(row=1,column=1,pady=3)

        ttk.Label(izquierda,text="Categoría").grid(row=2,column=0,sticky="w")
        self.categoria=ttk.Entry(izquierda,width=25)
        self.categoria.grid(row=2,column=1,pady=3)

        ttk.Label(izquierda,text="Precio").grid(row=3,column=0,sticky="w")
        self.precio=ttk.Entry(izquierda,width=25)
        self.precio.grid(row=3,column=1,pady=3)

        ttk.Label(izquierda,text="Stock").grid(row=4,column=0,sticky="w")
        self.stock=ttk.Entry(izquierda,width=25)
        self.stock.grid(row=4,column=1,pady=3)

        ttk.Button(
            izquierda,
            text="Registrar",
            command=self.registrar_producto
        ).grid(row=5,column=0,pady=10)

        ttk.Button(
            izquierda,
            text="Buscar",
            command=self.buscar_producto
        ).grid(row=5,column=1,pady=10)

        ttk.Button(
            izquierda,
            text="Actualizar",
            command=self.actualizar_producto
        ).grid(row=6,column=0,pady=5)

        ttk.Button(
            izquierda,
            text="Eliminar",
            command=self.eliminar_producto
        ).grid(row=6,column=1,pady=5)

        ttk.Button(
            izquierda,
            text="Cerrar sesión",
            command=self.salir
        ).grid(
            row=7,
            column=0,
            columnspan=2,
            pady=15
        )

        # --------------------------
        # DERECHA
        # --------------------------

        derecha = ttk.Frame(contenedor)

        derecha.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        productos_frame = ttk.LabelFrame(
            derecha,
            text="Productos"
        )

        productos_frame.pack(fill="both",expand=True)

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla = ttk.Treeview(
            productos_frame,
            columns=columnas,
            show="headings",
            height=10
        )

        for columna in columnas:

            self.tabla.heading(
                columna,
                text=columna.capitalize()
            )

            self.tabla.column(
                columna,
                width=100
            )

        scrollbar = ttk.Scrollbar(
            productos_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        self.tabla.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        usuarios_frame = ttk.LabelFrame(
            derecha,
            text="Usuarios"
        )

        usuarios_frame.pack(
            fill="x",
            pady=15
        )

        self.lista_usuarios = tk.Listbox(
            usuarios_frame,
            height=6
        )

        self.lista_usuarios.pack(
            fill="x"
        )

        self.cargar_productos()

        self.cargar_usuarios()
            def limpiar(self):

        self.codigo.delete(0,tk.END)
        self.nombre.delete(0,tk.END)
        self.categoria.delete(0,tk.END)
        self.precio.delete(0,tk.END)
        self.stock.delete(0,tk.END)

    def cargar_productos(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for producto in self.servicio.obtener_productos():

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    producto.precio,
                    producto.stock
                )
            )

    def cargar_usuarios(self):

        self.lista_usuarios.delete(
            0,
            tk.END
        )

        for usuario in self.servicio.obtener_usuarios():

            self.lista_usuarios.insert(
                tk.END,
                f"{usuario.identificacion} - {usuario.nombre}"
            )
                def registrar_producto(self):

        if self.servicio.registrar_producto(
            self.codigo.get(),
            self.nombre.get(),
            self.categoria.get(),
            self.precio.get(),
            self.stock.get()
        ):

            messagebox.showinfo(
                "Éxito",
                "Producto registrado."
            )

            self.cargar_productos()

            self.limpiar()

        else:

            messagebox.showerror(
                "Error",
                "El código ya existe."
            )

    def buscar_producto(self):

        producto = self.servicio.buscar_producto(
            self.codigo.get()
        )

        if producto is None:

            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )

            return

        self.nombre.delete(0,tk.END)
        self.nombre.insert(0,producto.nombre)

        self.categoria.delete(0,tk.END)
        self.categoria.insert(0,producto.categoria)

        self.precio.delete(0,tk.END)
        self.precio.insert(0,producto.precio)

        self.stock.delete(0,tk.END)
        self.stock.insert(0,producto.stock)

    def actualizar_producto(self):

        if self.servicio.actualizar_producto(

            self.codigo.get(),
            self.nombre.get(),
            self.categoria.get(),
            self.precio.get(),
            self.stock.get()

        ):

            messagebox.showinfo(
                "Éxito",
                "Producto actualizado."
            )

            self.cargar_productos()

        else:

            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )

    def eliminar_producto(self):

        if self.servicio.eliminar_producto(
            self.codigo.get()
        ):

            messagebox.showinfo(
                "Éxito",
                "Producto eliminado."
            )

            self.cargar_productos()

            self.limpiar()

        else:

            messagebox.showerror(
                "Error",
                "Producto no encontrado."
            )

    def salir(self):

        self.frame.destroy()

        self.cerrar_sesion()
