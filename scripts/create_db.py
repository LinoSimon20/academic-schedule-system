# Importamos sqlite3 para crear y gestionar la base de datos
import sqlite3
# Importamos os para operaciones del sistema operativo
import os

# Función para crear la base de datos con las tablas necesarias y datos de ejemplo
def crear_base_de_datos():

    # Nos aseguramos de que la carpeta database exista, si no la creamos
    os.makedirs("database", exist_ok=True)

    # Creamos la conexión a la base de datos SQLite
    conn = sqlite3.connect("database/academic_schedule.db")
    # Creamos el cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Activamos las claves foráneas para mantener integridad referencial
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Creamos la tabla tipos_usuario para almacenar tipos de usuarios (Admin, Estudiante, etc.)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tipos_usuario (
        id_tipo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE
    );
    """)

    # Creamos la tabla carreras para almacenar las carreras académicas disponibles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carreras (
        id_carrera INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE
    );
    """)

    # Creamos la tabla menciones para almacenar las menciones dentro de cada carrera
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menciones (
        id_mencion INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        id_carrera INTEGER,
        FOREIGN KEY (id_carrera) REFERENCES carreras(id_carrera)
    );
    """)

    # Creamos la tabla usuarios para almacenar la información de los usuarios del sistema
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        id_tipo INTEGER,
        id_carrera INTEGER,
        id_mencion INTEGER,
        FOREIGN KEY (id_tipo) REFERENCES tipos_usuario(id_tipo),
        FOREIGN KEY (id_carrera) REFERENCES carreras(id_carrera),
        FOREIGN KEY (id_mencion) REFERENCES menciones(id_mencion)
    );
    """)

    # Creamos la tabla materias para almacenar las asignaturas disponibles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materias (
        id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
        sigla TEXT,
        nombre TEXT NOT NULL
    );
    """)

    # Creamos la tabla dias para almacenar los días de la semana disponibles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dias (
        id_dia INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    );
    """)

    # Creamos la tabla horas para almacenar las horas de clase disponibles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS horas (
        id_hora INTEGER PRIMARY KEY AUTOINCREMENT,
        hora TEXT NOT NULL
    );
    """)

    # Creamos la tabla horario para almacenar los horarios de los estudiantes
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS horario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER,
        id_materia INTEGER,
        id_dia INTEGER,
        id_hora INTEGER,
        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
        FOREIGN KEY (id_materia) REFERENCES materias(id_materia),
        FOREIGN KEY (id_dia) REFERENCES dias(id_dia),
        FOREIGN KEY (id_hora) REFERENCES horas(id_hora)
    );
    """)

    # Creamos la tabla plan_estudios para almacenar el plan académico de cada carrera y mención
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS plan_estudios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_carrera INTEGER,
        id_materia INTEGER,
        id_mencion INTEGER,
        FOREIGN KEY (id_carrera) REFERENCES carreras(id_carrera),
        FOREIGN KEY (id_materia) REFERENCES materias(id_materia),
        FOREIGN KEY (id_mencion) REFERENCES menciones(id_mencion)
    );
    """)

    # Insertamos los tipos de usuario disponibles en el sistema
    cursor.execute("INSERT INTO tipos_usuario (nombre) VALUES ('Admin')")
    cursor.execute("INSERT INTO tipos_usuario (nombre) VALUES ('Estudiante')")

    # Insertamos una carrera de ejemplo
    cursor.execute("INSERT INTO carreras (nombre) VALUES ('Ingenieria de Sistemas')")

    # Insertamos una mención de ejemplo para la carrera de Ingeniería de Sistemas
    cursor.execute("""
    INSERT INTO menciones (nombre, id_carrera)
    VALUES ('General', 1)
    """)

    # Insertamos los días de la semana para usar en los horarios
    cursor.execute("INSERT INTO dias (nombre) VALUES ('Lunes')")
    cursor.execute("INSERT INTO dias (nombre) VALUES ('Martes')")
    cursor.execute("INSERT INTO dias (nombre) VALUES ('Miércoles')")
    cursor.execute("INSERT INTO dias (nombre) VALUES ('Jueves')")
    cursor.execute("INSERT INTO dias (nombre) VALUES ('Viernes')")

    # Insertamos las horas de clase disponibles
    cursor.execute("INSERT INTO horas (hora) VALUES ('08:00')")
    cursor.execute("INSERT INTO horas (hora) VALUES ('10:00')")
    cursor.execute("INSERT INTO horas (hora) VALUES ('12:00')")
    cursor.execute("INSERT INTO horas (hora) VALUES ('14:00')")
    cursor.execute("INSERT INTO horas (hora) VALUES ('16:00')")

    # Insertamos un usuario administrador de prueba
    cursor.execute("""
    INSERT INTO usuarios (nombre, password, id_tipo, id_carrera, id_mencion)
    VALUES ('admin', '1234', 1, 1, 1)
    """)

    # Insertamos un usuario estudiante de prueba
    cursor.execute("""
    INSERT INTO usuarios (nombre, password, id_tipo, id_carrera, id_mencion)
    VALUES ('estudiante', '1234', 2, 1, 1)
    """)
    
    # Confirmamos todos los cambios en la base de datos
    conn.commit()
    # Cerramos la conexión a la base de datos
    conn.close()

    # Mostramos un mensaje indicando que la base de datos se creó correctamente
    print("Base de datos creada correctamente")

# Punto de entrada del programa cuando se ejecuta directamente
if __name__ == "__main__":
    # Ejecutamos la función para crear la base de datos
    crear_base_de_datos()
