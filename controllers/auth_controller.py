from models.user_model import validar_usuario, seed_users

def iniciar():
    seed_users()  # inicializar la lista en memoria

def login(username, password):
    ok, user = validar_usuario(username, password)
    return ok, user

