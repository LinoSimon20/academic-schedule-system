# Importamos la función para obtener conexión a la base de datos desde el módulo db
from .db import obtener_conexion
# Importamos sqlite3 para manejo de errores específicos de la base de datos
import sqlite3

# Función para obtener todos los días de la semana disponibles en la base de datos
def obtener_dias():
    # Obtenemos conexión a la base de datos
    conn = obtener_conexion()
    # Creamos cursor para ejecutar consultas
    cursor = conn.cursor()
    try:
        # Ejecutamos consulta para obtener todos los días
        cursor.execute("SELECT id_dia, nombre FROM dias ORDER BY id_dia")
        # Almacenamos todos los resultados en una lista
        dias = cursor.fetchall()
    except sqlite3.Error as e:
        # Si hay error, mostramos el mensaje y retornamos lista vacía
        print(f"Error al obtener días: {e}")
        dias = []
    finally:
        # Cerramos la conexión en cualquier caso
        conn.close()
    # Retornamos la lista de días
    return dias

# Función para obtener todas las horas disponibles en la base de datos
def obtener_horas():
    # Obtenemos conexión a la base de datos
    conn = obtener_conexion()
    # Creamos cursor para ejecutar consultas
    cursor = conn.cursor()
    try:
        # Ejecutamos consulta para obtener todas las horas
        cursor.execute("SELECT id_hora, hora FROM horas ORDER BY id_hora")
        # Almacenamos todos los resultados en una lista
        horas = cursor.fetchall()
    except sqlite3.Error as e:
        # Si hay error, mostramos el mensaje y retornamos lista vacía
        print(f"Error al obtener horas: {e}")
        horas = []
    finally:
        # Cerramos la conexión en cualquier caso
        conn.close()
    # Retornamos la lista de horas
    return horas

# Función para obtener todos los materias disponibles en la base de datos
def obtener_materias_para_horario():
    # Obtenemos conexión a la base de datos
    conn = obtener_conexion()
    # Creamos cursor para ejecutar consultas
    cursor = conn.cursor()
    try:
        # Ejecutamos consulta para obtener todas las materias
        cursor.execute("SELECT id_materia, sigla, nombre FROM materias ORDER BY id_materia")
        # Almacenamos todos los resultados en una lista
        materias = cursor.fetchall()
    except sqlite3.Error as e:
        # Si hay error, mostramos el mensaje y retornamos lista vacía
        print(f"Error al obtener materias: {e}")
        materias = []
    finally:
        # Cerramos la conexión en cualquier caso
        conn.close()
    # Retornamos la lista de materias
    return materias

# Función para agregar una nueva entrada de horario para un usuario
def agregar_entrada_horario(id_usuario, id_materia, id_dia, id_hora):
    try:
        # Obtenemos conexión a la base de datos
        conn = obtener_conexion()
        # Creamos cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutamos consulta para insertar nueva entrada en tabla horario
        cursor.execute(
            """INSERT INTO horario (id_usuario, id_materia, id_dia, id_hora) 
               VALUES (?, ?, ?, ?)""",
            (id_usuario, id_materia, id_dia, id_hora)
        )
        # Confirmamos la transacción
        conn.commit()
        # Cerramos la conexión
        conn.close()
        # Retornamos True indicando éxito
        return True
    except sqlite3.Error as e:
        # Si hay error, mostramos el mensaje y retornamos False
        print(f"Error al agregar entrada de horario: {e}")
        return False

# Función para obtener el horario completo de un usuario
def obtener_horario_usuario(id_usuario):
    try:
        # Obtenemos conexión a la base de datos
        conn = obtener_conexion()
        # Creamos cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutamos consulta para obtener el horario del usuario con información completa
        cursor.execute(
            """SELECT h.id, m.sigla, m.nombre, d.nombre as dia, ho.hora
               FROM horario h
               JOIN materias m ON h.id_materia = m.id_materia
               JOIN dias d ON h.id_dia = d.id_dia
               JOIN horas ho ON h.id_hora = ho.id_hora
               WHERE h.id_usuario = ?
               ORDER BY d.id_dia, ho.id_hora""",
            (id_usuario,)
        )
        # Almacenamos todos los resultados en una lista
        horario = cursor.fetchall()
        # Cerramos la conexión
        conn.close()
        # Retornamos el horario del usuario
        return horario
    except sqlite3.Error as e:
        # Si hay error, mostramos el mensaje y retornamos lista vacía
        print(f"Error al obtener horario del usuario: {e}")
        return []

# Función para eliminar una entrada específica del horario
def eliminar_entrada_horario(id_horario):
    try:
        # Obtenemos conexión a la base de datos
        conn = obtener_conexion()
        # Creamos cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutamos consulta para eliminar una entrada específica de horario
        cursor.execute("DELETE FROM horario WHERE id = ?", (id_horario,))
        # Confirmamos la transacción
        conn.commit()
        # Verificamos si se eliminó algún registro (rowcount > 0 indica éxito)
        eliminado = cursor.rowcount > 0
        # Cerramos la conexión
        conn.close()
        # Retornamos si se eliminó o no
        return eliminado
    except sqlite3.Error as e:
        # Si hay error, mostramos el mensaje y retornamos False
        print(f"Error al eliminar entrada de horario: {e}")
        return False

# Función para verificar si existe una entrada de horario (evita duplicados)
def existe_entrada_horario(id_usuario, id_materia, id_dia, id_hora):
    try:
        # Obtenemos conexión a la base de datos
        conn = obtener_conexion()
        # Creamos cursor para ejecutar consultas
        cursor = conn.cursor()
        # Ejecutamos consulta para buscar si existe una entrada idéntica
        cursor.execute(
            """SELECT id FROM horario 
               WHERE id_usuario = ? AND id_materia = ? AND id_dia = ? AND id_hora = ?""",
            (id_usuario, id_materia, id_dia, id_hora)
        )
        # Verificamos si encontró algún resultado (existe o no)
        existe = cursor.fetchone() is not None
        # Cerramos la conexión
        conn.close()
        # Retornamos si existe o no
        return existe
    except sqlite3.Error as e:
        # Si hay error, mostramos el mensaje y retornamos False
        print(f"Error al verificar entrada de horario: {e}")
        return False
