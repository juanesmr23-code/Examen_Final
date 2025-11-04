import tkinter as tk
from tkinter import ttk, messagebox
from controllers.invernadero_controller import agregar_invernadero

class RegistrarInvernaderoView(tk.Frame):
    def __init__(self, master, user, control_view=None):
        super().__init__(master)
        self.user = user
        self.control_view = control_view  # Referencia a la vista de control para actualizar
        self.build()

    def build(self):
        # Imagen representativa del invernadero (Label con PhotoImage)
        try:
            from PIL import Image, ImageTk
            img = Image.open("assets/images/invernadero.png").resize((220, 150))
            self.invernadero_img = ImageTk.PhotoImage(img)
            tk.Label(self, image=self.invernadero_img).grid(row=0, column=0, columnspan=2, pady=(0, 10))
        except Exception:
            tk.Label(self, text="Invernadero", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

        tk.Label(self, text="Nombre").grid(row=1, column=0, sticky='w')
        self.nombre = tk.Entry(self); self.nombre.grid(row=1, column=1)

        tk.Label(self, text="Superficie (m2)").grid(row=2, column=0, sticky='w')
        self.superficie = tk.Entry(self); self.superficie.grid(row=2, column=1)

        tk.Label(self, text="Tipo cultivo").grid(row=3, column=0, sticky='w')
        self.tipo = ttk.Combobox(self, values=["Hortalizas","Ornamentales","Mix"])
        self.tipo.grid(row=3, column=1); self.tipo.current(0)

        tk.Label(self, text="Capacidad (ton)").grid(row=4, column=0, sticky='w')
        self.capacidad = tk.Entry(self); self.capacidad.grid(row=4, column=1)

        tk.Label(self, text="Sistema de riego").grid(row=5, column=0, sticky='w')
        self.riego = ttk.Combobox(self, values=["manual","automatizado","goteo"])
        self.riego.grid(row=5, column=1); self.riego.current(0)

        btn_guardar = tk.Button(self, text="Registrar",
                                command=lambda: self.registrar())
        btn_guardar.grid(row=6, column=0, columnspan=2, pady=10)

    def registrar(self):
        data = {
            'nombre': self.nombre.get(),
            'superficie': float(self.superficie.get() or 0),
            'tipo_cultivo': self.tipo.get(),
            'responsable': self.user['username'],
            'capacidad_ton': float(self.capacidad.get() or 0),
            'sistema_riego': self.riego.get()
        }
        agregar_invernadero(data)
        messagebox.showinfo("OK", "Invernadero registrado")
        # Limpiar campos
        self.nombre.delete(0, tk.END)
        self.superficie.delete(0, tk.END)
        self.capacidad.delete(0, tk.END)
        # Actualizar la vista de control si existe
        if self.control_view:
            self.control_view.cargar()

