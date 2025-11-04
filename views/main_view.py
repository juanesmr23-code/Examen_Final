import tkinter as tk
from tkinter import ttk
from views.registrar_invernadero_view import RegistrarInvernaderoView
from views.control_invernadero_view import ControlInvernaderoView
from views.control_humedad_view import ControlHumedadView
from views.control_piso_view import ControlPisoView
from controllers.invernadero_controller import obtener_invernaderos

class MainView(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user
        self.build()

    def build(self):
        # Top: logo en Label y bienvenida
        try:
            from PIL import Image, ImageTk
            img = Image.open("assets/logo.png").resize((80,80))
            self.logo_img = ImageTk.PhotoImage(img)
            tk.Label(self, image=self.logo_img).pack(side=tk.LEFT, padx=10, pady=10)
        except:
            tk.Label(self, text="GreenGrowth SA").pack(side=tk.LEFT)

        tk.Label(self, text=f"Usuario: {self.user['nombre']}").pack(anchor='ne')

        # Notebook (tabs)
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        tab_control = ControlInvernaderoView(notebook, self.user)
        tab_reg = RegistrarInvernaderoView(notebook, self.user, tab_control)
        # otros tabs
        tab_humedad = ControlHumedadView(notebook)
        tab_suelo = ControlPisoView(notebook)
        tab_enfermedades = tk.Frame(notebook)

        notebook.add(tab_reg, text="Registrar invernaderos")
        notebook.add(tab_control, text="Control invernadero")
        notebook.add(tab_humedad, text="Control de humedad")
        notebook.add(tab_suelo, text="Control de piso")
        notebook.add(tab_enfermedades, text="Enfermedades")

        # Dentro tab_enfermedades puedes incrustar la vista de manejo de dict->BD
        from views.enfermedades_view import EnfermedadesView
        ev = EnfermedadesView(tab_enfermedades)
        ev.pack(fill='both', expand=True)

        # Dashboard: simple summary
        btn_refresh = tk.Button(self, text="Actualizar dashboard",
                                command=lambda: self.update_dashboard())
        btn_refresh.pack(side=tk.BOTTOM, pady=5)

    def update_dashboard(self):
        inv = obtener_invernaderos()
        # aquí podrías actualizar widgets con counts, gráficos, etc.
        print("Total invernaderos:", len(inv))

