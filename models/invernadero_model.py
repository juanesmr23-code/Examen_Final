from models.conexion import conectar

def crear_invernadero(data):
    conn = conectar()
    cur = conn.cursor()
    sql = ("INSERT INTO invernaderos "
           "(nombre, superficie, tipo_cultivo, responsable, capacidad_ton, sistema_riego, estado) "
           "VALUES (%s,%s,%s,%s,%s,%s,%s)")
    cur.execute(sql, (
        data['nombre'], data['superficie'], data['tipo_cultivo'],
        data['responsable'], data['capacidad_ton'], data['sistema_riego'], data.get('estado','Operativo')
    ))
    conn.commit()
    cur.close(); conn.close()

def listar_invernaderos():
    conn = conectar()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM invernaderos")
    rows = cur.fetchall()
    cur.close(); conn.close()
    return rows

def obtener_invernadero_por_id(id_):
    conn = conectar()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM invernaderos WHERE id=%s", (id_,))
    row = cur.fetchone()
    cur.close(); conn.close()
    return row

def actualizar_invernadero(id_, data):
    conn = conectar()
    cur = conn.cursor()
    sql = ("UPDATE invernaderos SET nombre=%s, superficie=%s, tipo_cultivo=%s, responsable=%s, capacidad_ton=%s, sistema_riego=%s, estado=%s "
           "WHERE id=%s")
    cur.execute(sql, (
        data['nombre'], data['superficie'], data['tipo_cultivo'], data['responsable'],
        data['capacidad_ton'], data['sistema_riego'], data['estado'], id_
    ))
    conn.commit()
    cur.close(); conn.close()

def eliminar_invernadero(id_):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM invernaderos WHERE id=%s", (id_,))
    conn.commit()
    cur.close(); conn.close()

