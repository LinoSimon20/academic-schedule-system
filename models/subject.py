# Importamos la función para obtener conexión a la base de datos
from .db import obtener_conexion

# Función para obtener todas las materias registradas en la base de datos
def obtener_materias():
    # Obtenemos una conexión a la base de datos
    conn = obtener_conexion()
    # Creamos un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutamos consulta para obtener todas las materias (sigla y nombre)
    cursor.execute("SELECT sigla, nombre FROM materias")
    # Almacenamos todos los resultados en una lista
    materias = cursor.fetchall()
    # Cerramos la conexión
    conn.close()
    # Retornamos la lista de materias
    return materias

# Función para insertar una nueva materia en la base de datos
def insertar_materia(sigla, nombre):
    try:
        # Obtenemos una conexión a la base de datos
        conn = obtener_conexion()
        # Creamos un cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutamos consulta para insertar una nueva materia
        cursor.execute(
            "INSERT INTO materias (sigla, nombre) VALUES (?, ?)",
            (sigla, nombre),
        )
        # Confirmamos la transacción
        conn.commit()
        # Cerramos la conexión
        conn.close()
        # Retornamos True indicando éxito
        return True
    except Exception:
        # Si hay error de cualquier tipo, retornamos False
        return False

# Función para eliminar una materia de la base de datos
def eliminar_materia(sigla):
    # Obtenemos una conexión a la base de datos
    conn = obtener_conexion()
    # Creamos un cursor para ejecutar consultas
    cursor = conn.cursor()
    # Ejecutamos consulta para eliminar una materia por sigla
    cursor.execute("DELETE FROM materias WHERE sigla = ?", (sigla,))
    # Verificamos si se eliminó algún registro (rowcount > 0 indica éxito)
    eliminado = cursor.rowcount > 0
    # Confirmamos la transacción
    conn.commit()
    # Cerramos la conexión
    conn.close()
    # Retornamos si se eliminó o no
    return eliminado
