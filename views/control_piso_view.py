import tkinter as tk
from tkinter import ttk

class ControlPisoView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build()

    def build(self):
        toolbar = tk.Frame(self); toolbar.pack(fill='x', pady=5)
        tk.Label(toolbar, text="Zona").pack(side='left')
        self.cbo_zona = ttk.Combobox(toolbar, values=["Norte","Centro","Sur"]); self.cbo_zona.current(0)
        self.cbo_zona.pack(side='left', padx=5)
        tk.Button(toolbar, text="Cargar", command=lambda: self.cargar()).pack(side='left', padx=5)

        self.tree = ttk.Treeview(self, columns=("fecha","estado"), show="headings")
        self.tree.heading("fecha", text="Fecha/Hora"); self.tree.heading("estado", text="Estado")
        self.tree.pack(fill='both', expand=True)
        self.cargar()

    def cargar(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        datos = [("2025-11-03 10:00", "Seco"), ("2025-11-03 11:00", "Húmedo"), ("2025-11-03 12:00", "Óptimo")]
        for f, e in datos:
            self.tree.insert("", "end", values=(f, e))
