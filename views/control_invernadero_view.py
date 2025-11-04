import tkinter as tk
from tkinter import ttk, messagebox
from controllers.invernadero_controller import obtener_invernaderos, editar_invernadero, borrar_invernadero, obtener_invernadero

class ControlInvernaderoView(tk.Frame):
    def __init__(self, master, user):
        super().__init__(master)
        self.user = user
        self.build()

    def build(self):
        self.tree = ttk.Treeview(self, columns=('id','nombre','estado'), show='headings')
        self.tree.heading('id', text='ID'); self.tree.heading('nombre', text='Nombre'); self.tree.heading('estado', text='Estado')
        self.tree.pack(fill='both', expand=True)

        frm = tk.Frame(self)
        frm.pack(pady=5)
        tk.Button(frm, text="Ver", command=lambda: self.ver()).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Editar", command=lambda: self.editar()).pack(side=tk.LEFT, padx=5)
        tk.Button(frm, text="Eliminar", command=lambda: self.eliminar()).pack(side=tk.LEFT, padx=5)

        self.cargar()

    def cargar(self):
        for i in self.tree.get_children(): self.tree.delete(i)
        for inv in obtener_invernaderos():
            self.tree.insert('', 'end', values=(inv['id'], inv['nombre'], inv['estado']))

    def ver(self):
        sel = self.tree.selection()
        if not sel: return
        vals = self.tree.item(sel[0])['values']
        messagebox.showinfo("Detalles", f"ID:{vals[0]} Nombre:{vals[1]} Estado:{vals[2]}")

    def editar(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Advertencia", "Selecciona un invernadero para editar")
            return
        
        id_ = self.tree.item(sel[0])['values'][0]
        # Obtener datos actuales del invernadero
        inv_actual = obtener_invernadero(id_)
        
        if not inv_actual:
            messagebox.showerror("Error", "No se pudo obtener los datos del invernadero")
            return
        
        # Crear ventana de edición
        dialog = tk.Toplevel(self)
        dialog.title("Editar Invernadero")
        dialog.geometry("400x300")
        
        # Nombre
        tk.Label(dialog, text="Nombre:").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        entry_nombre = tk.Entry(dialog, width=30)
        entry_nombre.insert(0, inv_actual['nombre'] or '')
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        # Superficie
        tk.Label(dialog, text="Superficie (m²):").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        entry_superficie = tk.Entry(dialog, width=30)
        entry_superficie.insert(0, str(inv_actual['superficie'] or 0))
        entry_superficie.grid(row=1, column=1, padx=5, pady=5)
        
        # Tipo cultivo
        tk.Label(dialog, text="Tipo cultivo:").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        combo_tipo = ttk.Combobox(dialog, values=["Hortalizas","Ornamentales","Mix"], width=27)
        combo_tipo.set(inv_actual['tipo_cultivo'] or 'Hortalizas')
        combo_tipo.grid(row=2, column=1, padx=5, pady=5)
        
        # Capacidad
        tk.Label(dialog, text="Capacidad (ton):").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        entry_capacidad = tk.Entry(dialog, width=30)
        entry_capacidad.insert(0, str(inv_actual['capacidad_ton'] or 0))
        entry_capacidad.grid(row=3, column=1, padx=5, pady=5)
        
        # Sistema riego
        tk.Label(dialog, text="Sistema de riego:").grid(row=4, column=0, sticky='w', padx=5, pady=5)
        combo_riego = ttk.Combobox(dialog, values=["manual","automatizado","goteo"], width=27)
        combo_riego.set(inv_actual['sistema_riego'] or 'manual')
        combo_riego.grid(row=4, column=1, padx=5, pady=5)
        
        # Estado
        tk.Label(dialog, text="Estado:").grid(row=5, column=0, sticky='w', padx=5, pady=5)
        combo_estado = ttk.Combobox(dialog, values=["Operativo","Reparación","Inspección","Expansión"], width=27)
        combo_estado.set(inv_actual['estado'] or 'Operativo')
        combo_estado.grid(row=5, column=1, padx=5, pady=5)
        
        def guardar_edicion():
            try:
                data = {
                    'nombre': entry_nombre.get(),
                    'superficie': float(entry_superficie.get() or 0),
                    'tipo_cultivo': combo_tipo.get(),
                    'responsable': inv_actual['responsable'] or self.user['username'],
                    'capacidad_ton': float(entry_capacidad.get() or 0),
                    'sistema_riego': combo_riego.get(),
                    'estado': combo_estado.get()
                }
                editar_invernadero(id_, data)
                self.cargar()
                dialog.destroy()
                messagebox.showinfo("OK", "Invernadero actualizado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"Error al actualizar: {str(e)}")
        
        btn_frame = tk.Frame(dialog)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)
        tk.Button(btn_frame, text="Guardar", command=guardar_edicion).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Cancelar", command=dialog.destroy).pack(side=tk.LEFT, padx=5)

    def eliminar(self):
        sel = self.tree.selection()
        if not sel: return
        id_ = self.tree.item(sel[0])['values'][0]
        borrar_invernadero(id_)
        self.cargar()
        messagebox.showinfo("OK", "Eliminado")

