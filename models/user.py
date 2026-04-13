from .db import obtener_conexion
import sqlite3

def buscar_usuario(nombre, password):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id_usuario, nombre FROM usuarios WHERE nombre = ? AND password = ?",
            (nombre, password),
        )
        usuario = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Error al buscar usuario: {e}")
        usuario = None
    finally:
        conn.close()
    return usuario


def existe_usuario(nombre):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre = ?", (nombre,))
        existe = cursor.fetchone() is not None
    except sqlite3.Error as e:
        print(f"Error al verificar existencia de usuario: {e}")
        existe = False
    finally:
        conn.close()
    return existe


def crear_usuario(nombre, password, id_tipo=2, id_carrera=1, id_mencion=1):
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, password, id_tipo, id_carrera, id_mencion) VALUES (?, ?, ?, ?, ?)",
            (nombre, password, id_tipo, id_carrera, id_mencion),
        )
    except sqlite3.Error as e:
        print(f"Error al crear usuario: {e}")
    finally:
        conn.close()
    conn.commit()
    conn.close()
    return True
