import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',     # usuario XAMPP
            password='',     # si tiene contraseña, colocarla
            database='greengrowth'
        )
        return conn
    except Error as e:
        print("Error conexión:", e)
        return None

