from models.subject import obtener_materias, insertar_materia, eliminar_materia
from views.schedule_view import (
    mostrar_materias_lista,
    mostrar_materia_agregada,
    mostrar_materia_eliminada,
    mostrar_error_materia,
)

def mostrar_materias():
    materias = obtener_materias()
    mostrar_materias_lista(materias)

def agregar_materia():
    sigla = input("Ingrese la sigla de la materia: ").strip()
    nombre = input("Ingrese el nombre de la materia: ").strip()
    if not sigla or not nombre:
        mostrar_error_materia("La sigla y el nombre son obligatorios.")
        return
    if insertar_materia(sigla, nombre):
        mostrar_materia_agregada(sigla, nombre)
    else:
        mostrar_error_materia("No se pudo agregar la materia. Verifique los datos.")

def eliminar_materia():
    sigla = input("Ingrese la sigla de la materia a eliminar: ").strip()
    if not sigla:
        mostrar_error_materia("La sigla es obligatoria.")
        return
    if eliminar_materia(sigla):
        mostrar_materia_eliminada(sigla)
    else:
        mostrar_error_materia("No se encontró la materia con esa sigla.")
