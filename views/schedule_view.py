def mostrar_materias_lista(materias):
    print("Materias disponibles:")
    print("Sigla | Nombre")
    if not materias:
        print("No hay materias registradas.")
        return
    for sigla, nombre in materias:
        print(f"{sigla} | {nombre}")


def mostrar_materia_agregada(sigla, nombre):
    print(f"Materia agregada: {sigla} - {nombre}")


def mostrar_materia_eliminada(sigla):
    print(f"Materia eliminada: {sigla}")


def mostrar_error_materia(mensaje):
    print(f"Error: {mensaje}")
