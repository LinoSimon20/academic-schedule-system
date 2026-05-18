# Importamos la función para obtener conexión a la base de datos
from .db import obtener_conexion
# Importamos sqlite3 para manejo de errores específicos de la base de datos
import sqlite3

# Función para buscar un usuario por nombre y contraseña en la base de datos
def buscar_usuario(nombre, password):
    # Obtenemos una conexión a la base de datos
    conn = obtener_conexion()
    # Creamos un cursor para ejecutar consultas
    cursor = conn.cursor()
    try:
        # Ejecutamos consulta para buscar el usuario con nombre y contraseña coincidentes
        # El ? se usa para evitar inyección SQL, parametrizando las variables
        cursor.execute(
            "SELECT id_usuario, nombre FROM usuarios WHERE nombre = ? AND password = ?",
            (nombre, password),
        )
        # Obtenemos el primer resultado (si existe)
        usuario = cursor.fetchone()
    except sqlite3.Error as e:
        # Si hay error en la base de datos, imprimimos el mensaje y asignamos None
        print(f"Error al buscar usuario: {e}")
        usuario = None
    finally:
        # Cerramos la conexión en cualquier caso (éxito o error)
        conn.close()
    # Retornamos el usuario encontrado o None si no existe
    return usuario

# Función para verificar si un usuario existe en la base de datos
def existe_usuario(nombre):
    # Obtenemos una conexión a la base de datos
    conn = obtener_conexion()
    # Creamos un cursor para ejecutar consultas
    cursor = conn.cursor()
    try:
        # Ejecutamos consulta para buscar si existe un usuario con ese nombre
        cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre = ?", (nombre,))
        # Verificamos si fetchone() retorna algo (True si existe, False si no)
        existe = cursor.fetchone() is not None
    except sqlite3.Error as e:
        # Si hay error en la base de datos, imprimimos el mensaje e indicamos que no existe
        print(f"Error al verificar existencia de usuario: {e}")
        existe = False
    finally:
        # Cerramos la conexión en cualquier caso (éxito o error)
        conn.close()
    # Retornamos si el usuario existe o no
    return existe

# Función para crear un nuevo usuario en la base de datos
def crear_usuario(nombre, password, id_tipo=2, id_carrera=1, id_mencion=1):
    # Obtenemos una conexión a la base de datos
    conn = obtener_conexion()
    # Creamos un cursor para ejecutar consultas
    cursor = conn.cursor()
    try:
        # Ejecutamos consulta para insertar un nuevo usuario
        # Por defecto, id_tipo=2 significa "Estudiante", id_carrera=1 y id_mencion=1
        cursor.execute(
            """INSERT INTO usuarios (nombre, password, id_tipo, id_carrera, id_mencion) 
               VALUES (?, ?, ?, ?, ?)""",
            (nombre, password, id_tipo, id_carrera, id_mencion),
        )
    except sqlite3.Error as e:
        # Si hay error en la base de datos, imprimimos el mensaje
        print(f"Error al crear usuario: {e}")
    finally:
        # Confirmamos la transacción
        conn.commit()
        # Cerramos la conexión
        conn.close()
    # Retornamos True indicando que se ejecutó la función
    return True

