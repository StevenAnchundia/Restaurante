import tkinter as tk
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from servicios import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def iniciar_aplicacion():
    servicio = RestauranteServicio()
    raiz = tk.Tk()
    raiz.withdraw()

    def al_autenticar(usuario):
        # Mostrar ventana principal
        ventana_principal = MainView(raiz, servicio, usuario)
        ventana_principal.protocol("WM_DELETE_WINDOW", raiz.destroy)
        raiz.withdraw()

    login = LoginView(servicio, al_autenticar)
    login.mainloop()


if __name__ == "__main__":
    iniciar_aplicacion()