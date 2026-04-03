#Conectar base de datos
import sqlite3
def obtener_conexion():
    return sqlite3.connect("database/academic_schedule.db")
