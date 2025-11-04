import tkinter as tk
from tkinter import ttk

class ControlHumedadView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.build()

    def build(self):
        toolbar = tk.Frame(self); toolbar.pack(fill='x', pady=5)
        tk.Label(toolbar, text="Sensor").pack(side='left')
        self.cbo_sensor = ttk.Combobox(toolbar, values=["H1","H2","H3"]); self.cbo_sensor.current(0)
        self.cbo_sensor.pack(side='left', padx=5)
        tk.Button(toolbar, text="Cargar", command=lambda: self.cargar()).pack(side='left', padx=5)

        self.tree = ttk.Treeview(self, columns=("fecha","humedad"), show="headings")
        self.tree.heading("fecha", text="Fecha/Hora"); self.tree.heading("humedad", text="% Humedad")
        self.tree.pack(fill='both', expand=True)
        self.cargar()

    def cargar(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        datos = [("2025-11-03 10:00", 58), ("2025-11-03 11:00", 60), ("2025-11-03 12:00", 63)]
        for f, h in datos:
            self.tree.insert("", "end", values=(f, h))
