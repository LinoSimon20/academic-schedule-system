import os
import time
from views.menu_view import (
    mostrar_bienvenida,
    mostrar_menu_principal,
    mostrar_opcion_invalida,
)
from controllers.schedule_controller import mostrar_materias, agregar_materia, eliminar_materia

def mostrar_menu(usuario):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_bienvenida(usuario)
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            os.system("cls" if os.name == "nt" else "clear")
            mostrar_materias()
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            os.system("cls" if os.name == "nt" else "clear")
            agregar_materia()
        elif opcion == "3":
            os.system("cls" if os.name == "nt" else "clear")
            eliminar_materia()
        elif opcion == "4":
            print("Saliendo...")
            time.sleep(1)
            os.system("cls" if os.name == "nt" else "clear")
            return
        else:
            mostrar_opcion_invalida()
            input("Presione Enter...")
