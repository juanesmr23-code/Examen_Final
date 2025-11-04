import tkinter as tk
from controllers.auth_controller import iniciar
from views.login_view import LoginView
from views.main_view import MainView

def main():
    iniciar()  # seed usuarios
    root = tk.Tk()
    root.title("GreenGrowth SA - Sistema")
    root.geometry("1000x700")

    def on_login(user):
        # limpia la ventana y carga el main
        for w in root.winfo_children(): w.destroy()
        main_view = MainView(root, user)
        main_view.pack(fill='both', expand=True)

    login = LoginView(root, on_login)
    login.pack(fill='both', expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()

