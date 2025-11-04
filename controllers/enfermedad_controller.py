# Diccionario en memoria: {clave_id: {nombre, descripcion, gravedad}}
dict_enfermedades = {}
_id_counter = 1

from models.enfermedad_model import guardar_enfermedad_db

def agregar_en_memoria(nombre, descripcion, gravedad):
    global _id_counter
    dict_enfermedades[_id_counter] = {'nombre': nombre, 'descripcion': descripcion, 'gravedad': gravedad}
    _id_counter += 1

def pasar_a_bd():
    for k, v in dict_enfermedades.items():
        guardar_enfermedad_db(v['nombre'], v['descripcion'], v['gravedad'])
    # opcional: limpiar el dict después de persistir
    dict_enfermedades.clear()

