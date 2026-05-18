# Importamos sqlite3 para conexión a base de datos
import sqlite3
# Importamos Path de pathlib para manejo de rutas de forma multiplataforma
from pathlib import Path

# Definimos la ruta donde se guarda la base de datos SQLite
# Path(__file__).resolve().parent.parent obtiene el directorio padre del proyecto
# Luego accedemos a la carpeta database y el archivo academic_schedule.db
DB_PATH = Path(__file__).resolve().parent.parent / "database" / "academic_schedule.db"

# Función para obtener una conexión con la base de datos
def obtener_conexion():
    try:
        # Intentamos crear y retornar una conexión a la base de datos SQLite
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        # Si hay un error, imprimimos el mensaje de error
        print(f"Error al conectar a la base de datos: {e}")
        # Retornamos None si no se puede conectar
        return None

