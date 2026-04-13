from .db import obtener_conexion

def obtener_materias():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT sigla, nombre FROM materias")
    materias = cursor.fetchall()
    conn.close()
    return materias


def insertar_materia(sigla, nombre):
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO materias (sigla, nombre) VALUES (?, ?)",
            (sigla, nombre),
        )
        conn.commit()
        conn.close()
        return True
    except Exception:
        return False


def eliminar_materia(sigla):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM materias WHERE sigla = ?", (sigla,))
    eliminado = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return eliminado
