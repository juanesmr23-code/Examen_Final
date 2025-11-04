from models.conexion import conectar

def guardar_enfermedad_db(nombre, descripcion, gravedad):
    conn = conectar()
    cur = conn.cursor()
    sql = "INSERT INTO enfermedades (nombre, descripcion, gravedad) VALUES (%s,%s,%s)"
    cur.execute(sql, (nombre, descripcion, gravedad))
    conn.commit()
    cur.close(); conn.close()

def listar_enfermedades_db():
    conn = conectar()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM enfermedades")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows

