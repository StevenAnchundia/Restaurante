import tkinter as tk

from servicios import RestauranteServicio

from ui import LoginView
from ui import MainView


class RestauranteApp:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("Restaurante App")

        self.root.geometry("950x600")

        self.root.resizable(False, False)

        self.servicio = RestauranteServicio()

        self.mostrar_login()

        self.root.mainloop()

    # ======================================
    # LOGIN
    # ======================================

    def mostrar_login(self):

        LoginView(

            self.root,

            self.servicio,

            self.mostrar_main

        )

    # ======================================
    # MAIN
    # ======================================

    def mostrar_main(self):

        MainView(

            self.root,

            self.servicio,

            self.mostrar_login

        )


if __name__ == "__main__":

    RestauranteApp()
