import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Restaurante App")

        self.root.geometry("700x600")

        self.root.resizable(False, False)

        # Servicio
        self.restaurante_servicio = RestauranteServicio()

        # Vistas
        self.login_view = LoginView(
            self.root,
            self.restaurante_servicio
        )

        self.main_view = MainView(
            self.root,
            self.restaurante_servicio
        )

        # Eventos
        self.login_view.on_login = self.mostrar_main

        self.main_view.on_logout = self.mostrar_login

        # Mostrar Login
        self.mostrar_login()

    def mostrar_login(self):

        self.main_view.ocultar()

        self.login_view.mostrar()

    def mostrar_main(self):

        self.login_view.ocultar()

        self.main_view.mostrar()


def main():

    root = tk.Tk()

    RestauranteApp(root)

    root.mainloop()


if __name__ == "__main__":

    main()
