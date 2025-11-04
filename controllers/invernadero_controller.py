from models.invernadero_model import crear_invernadero, listar_invernaderos, actualizar_invernadero, eliminar_invernadero, obtener_invernadero_por_id

def agregar_invernadero(data):
    crear_invernadero(data)

def obtener_invernaderos():
    return listar_invernaderos()

def editar_invernadero(id_, data):
    actualizar_invernadero(id_, data)

def borrar_invernadero(id_):
    eliminar_invernadero(id_)

def obtener_invernadero(id_):
    return obtener_invernadero_por_id(id_)

