import os, schedule_manager, time

# Menú principal
os.system("cls")
def mostrar_menu(usuario):
    import os
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Bienvenido al sistema de horarios", usuario[1], "!")
        print("1. Ver materias")
        print("2. Agregar materia")
        print("3. Eliminar materia")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            os.system("cls")
            schedule_manager.mostrar_materias()
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            os.system("cls")
            schedule_manager.agregar_materia()
        elif opcion == "3":
            os.system("cls")
            schedule_manager.eliminar_materia()
        elif opcion == "4":
            print("Saliendo...")
            time.sleep(1)
            os.system("cls")
            return
        else:
            print("Opción inválida")
            input("Presione Enter...")