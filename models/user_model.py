import hashlib
from models.conexion import conectar

# Lista de usuarios en memoria (username, password_hash, nombre)
USUARIOS = []

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def seed_users():
    # Ejemplo: usuarios por defecto
    global USUARIOS
    USUARIOS = [
        {'username': 'admin', 'password_hash': hash_password('admin123'), 'nombre': 'Administrador'},
        {'username': 'juan', 'password_hash': hash_password('juan1234'), 'nombre': 'Juan Perez'}
    ]

def validar_usuario(username, password):
    pw_hash = hash_password(password)
    for u in USUARIOS:
        if u['username'] == username and u['password_hash'] == pw_hash:
            return True, u
    return False, None

# Opcional: cargar usuarios desde BD (si quieres sincronizar)
def cargar_usuarios_desde_bd():
    conn = conectar()
    if not conn: return
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT username, password_hash, nombre FROM usuarios")
    rows = cur.fetchall()
    cur.close(); conn.close()
    global USUARIOS
    USUARIOS = rows

