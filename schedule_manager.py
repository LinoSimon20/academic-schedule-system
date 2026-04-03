import connection_db

#Leer datos
def mostrar_materias():
    conn = connection_db.obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT sigla, nombre " \
                    "FROM materias")
    materias = cursor.fetchall()
    print("Materias disponibles:")
    print("Sigla | Nombre")
    for m in materias:
        print(m)

#Agregar materia
def agregar_materia():
    print("Agregar materia")

#Eliminar materia
def eliminar_materia():
    print("Eliminar materia")