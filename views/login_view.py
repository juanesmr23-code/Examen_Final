import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # si usas Pillow para PNG/escala
from controllers import auth_controller

class LoginView(tk.Frame):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.on_login_success = on_login_success
        self.build()

    def build(self):
        # Logo con Label (usar PhotoImage)
        try:
            img = Image.open("assets/logo.png").resize((150,150))
            self.logo_img = ImageTk.PhotoImage(img)
            lbl_logo = tk.Label(self, image=self.logo_img)
            lbl_logo.pack(pady=10)
        except Exception as e:
            tk.Label(self, text="GreenGrowth SA", font=("Arial",18)).pack(pady=10)

        tk.Label(self, text="Usuario").pack()
        self.entry_user = tk.Entry(self)
        self.entry_user.pack()

        tk.Label(self, text="Contraseña").pack()
        self.entry_pass = tk.Entry(self, show="*")
        self.entry_pass.pack()

        btn_login = tk.Button(self, text="Ingresar",
                              command=lambda: self.do_login())
        btn_login.pack(pady=10)

    def do_login(self):
        from controllers.auth_controller import login
        user = self.entry_user.get()
        pwd = self.entry_pass.get()
        ok, user_obj = login(user, pwd)
        if ok:
            messagebox.showinfo("OK", f"Bienvenido {user_obj['nombre']}")
            self.on_login_success(user_obj)
        else:
            messagebox.showerror("Error", "Usuario o contraseña inválidos")

