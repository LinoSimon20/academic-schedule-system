import sqlite3, os

# Funcion para crear la base de datos con las tablas necesarias y datos de ejemplo
def crear_base_de_datos():

    # Aseguramos de que la carpeta database exista
    os.makedirs("database", exist_ok=True)

    # Creamos la conexion a la base de datos
    conn = sqlite3.connect("database/academic_schedule.db")
    cursor = conn.cursor()

    # Activar claves foráneas
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Tabla tipos de usuario
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tipos_usuario (
        id_tipo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE
    );
    """)

    # Tabla carreras
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carreras (
        id_carrera INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL UNIQUE
    );
    """)

    # Tabla menciones
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS menciones (
        id_mencion INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        id_carrera INTEGER,
        FOREIGN KEY (id_carrera) REFERENCES carreras(id_carrera)
    );
    """)

    # Tabla usuarios
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

    # Tabla materias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS materias (
        id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
        sigla TEXT,
        nombre TEXT NOT NULL
    );
    """)

    # Tabla dias
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dias (
        id_dia INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    );
    """)

    # Tabla horas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS horas (
        id_hora INTEGER PRIMARY KEY AUTOINCREMENT,
        hora TEXT NOT NULL
    );
    """)

    # Tabla horario
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

    # Tabla plan de estudios
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

    # Insertar tipos de usuario
    cursor.execute("INSERT INTO tipos_usuario (nombre) VALUES ('Admin')")
    cursor.execute("INSERT INTO tipos_usuario (nombre) VALUES ('Estudiante')")

    # Insertar carrera de ejemplo
    cursor.execute("INSERT INTO carreras (nombre) VALUES ('Ingenieria de Sistemas')")

    # Insertar mención de ejemplo
    cursor.execute("""
    INSERT INTO menciones (nombre, id_carrera)
    VALUES ('General', 1)
    """)

    # Insertar usuarios
    cursor.execute("""
    INSERT INTO usuarios (nombre, password, id_tipo, id_carrera, id_mencion)
    VALUES ('admin', '1234', 1, 1, 1)
    """)

    cursor.execute("""
    INSERT INTO usuarios (nombre, password, id_tipo, id_carrera, id_mencion)
    VALUES ('estudiante', '1234', 2, 1, 1)
    """)
    
    conn.commit()
    conn.close()

    print("Base de datos creada correctamente")

# Invocamos la funcion para crear la base de datos 
if __name__ == "__main__":
    crear_base_de_datos()