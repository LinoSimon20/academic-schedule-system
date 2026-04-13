import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "database" / "academic_schedule.db"

def obtener_conexion():
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
