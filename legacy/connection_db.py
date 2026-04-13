#Conectar base de datos
import sqlite3
def obtener_conexion():
    try:
        return sqlite3.connect("database/academic_schedule.db")
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None