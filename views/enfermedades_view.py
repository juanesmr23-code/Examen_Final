import tkinter as tk
from tkinter import messagebox, ttk
from controllers.enfermedad_controller import agregar_en_memoria, pasar_a_bd, dict_enfermedades
from models.enfermedad_model import listar_enfermedades_db

class EnfermedadesView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build()

    def build(self):
        tk.Label(self, text="Nombre").grid(row=0, column=0)
        self.nombre = tk.Entry(self); self.nombre.grid(row=0, column=1)
        tk.Label(self, text="Descripción").grid(row=1, column=0)
        self.desc = tk.Entry(self); self.desc.grid(row=1, column=1)
        tk.Label(self, text="Gravedad").grid(row=2, column=0)
        self.grav = ttk.Combobox(self, values=["Baja","Media","Alta"]); self.grav.grid(row=2, column=1); self.grav.current(0)

        tk.Button(self, text="Agregar en memoria", command=lambda: self.add_mem()).grid(row=3, column=0, pady=5)
        tk.Button(self, text="Persistir a BD", command=lambda: self.save_db()).grid(row=3, column=1, pady=5)

        self.tree = ttk.Treeview(self, columns=('id','nombre','grav'), show='headings')
        self.tree.heading('id', text='ID'); self.tree.heading('nombre', text='Nombre'); self.tree.heading('grav', text='Gravedad')
        self.tree.grid(row=4, column=0, columnspan=2, sticky='nsew')

        tk.Button(self, text="Cargar desde BD", command=lambda: self.cargar_bd()).grid(row=5, column=0, columnspan=2)

    def add_mem(self):
        agregar_en_memoria(self.nombre.get(), self.desc.get(), self.grav.get())
        messagebox.showinfo("OK","Enfermedad agregada en memoria")

    def save_db(self):
        pasar_a_bd()
        messagebox.showinfo("OK","Enfermedades persistidas a BD")

    def cargar_bd(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        rows = listar_enfermedades_db()
        for r in rows:
            self.tree.insert('', 'end', values=(r['id'], r['nombre'], r['gravedad']))

