# Importamos el módulo os para limpiar la pantalla
import os
# Importamos el módulo time para hacer pausas
import time
# Importamos las funciones de vista para mostrar el menú y mensajes
from views.menu_view import (
    mostrar_bienvenida,
    mostrar_menu_principal,
    mostrar_opcion_invalida,
)
# Importamos las funciones del controlador de horarios
from controllers.schedule_controller import (
    mostrar_materias, 
    agregar_materia, 
    eliminar_materia,
    crear_horario,
    consultar_horario
)

# Función principal que muestra el menú y gestiona la navegación del usuario
def mostrar_menu(usuario):
    # Obtenemos el id del usuario de la tupla retornada por la autenticación
    id_usuario = usuario[0]
    # Iniciamos un bucle infinito para mostrar el menú continuamente
    while True:
        # Limpiamos la pantalla (cls en Windows, clear en Linux/Mac)
        os.system("cls" if os.name == "nt" else "clear")
        # Mostramos el mensaje de bienvenida con el nombre del usuario
        mostrar_bienvenida(usuario)
        # Mostramos las opciones disponibles en el menú principal
        mostrar_menu_principal()
        # Solicitamos al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ").strip()

        # Si selecciona opción 1, muestra las materias disponibles
        if opcion == "1":
            # Limpiamos la pantalla
            os.system("cls" if os.name == "nt" else "clear")
            # Llamamos a la función para mostrar materias
            mostrar_materias()
            # Esperamos a que el usuario presione Enter para continuar
            input("\nPresione Enter para continuar...")
        
        # Si selecciona opción 2, agrega una nueva materia
        elif opcion == "2":
            # Limpiamos la pantalla
            os.system("cls" if os.name == "nt" else "clear")
            # Llamamos a la función para agregar materia
            agregar_materia()
            # Esperamos a que el usuario presione Enter para continuar
            input("\nPresione Enter para continuar...")
        
        # Si selecciona opción 3, elimina una materia
        elif opcion == "3":
            # Limpiamos la pantalla
            os.system("cls" if os.name == "nt" else "clear")
            # Llamamos a la función para eliminar materia
            eliminar_materia()
            # Esperamos a que el usuario presione Enter para continuar
            input("\nPresione Enter para continuar...")
        
        # Si selecciona opción 4, crea un nuevo horario
        elif opcion == "4":
            # Limpiamos la pantalla
            os.system("cls" if os.name == "nt" else "clear")
            # Llamamos a la función para crear una entrada de horario
            crear_horario(id_usuario)
            # Esperamos a que el usuario presione Enter para continuar
            input("\nPresione Enter para continuar...")
        
        # Si selecciona opción 5, consulta el horario existente
        elif opcion == "5":
            # Limpiamos la pantalla
            os.system("cls" if os.name == "nt" else "clear")
            # Llamamos a la función para consultar el horario del usuario
            consultar_horario(id_usuario)
            # Esperamos a que el usuario presione Enter para continuar
            input("\nPresione Enter para continuar...")
        
        # Si selecciona opción 6, sale del sistema
        elif opcion == "6":
            # Mostramos un mensaje indicando que se está saliendo
            print("Saliendo...")
            # Hacemos una pausa de 1 segundo
            time.sleep(1)
            # Limpiamos la pantalla
            os.system("cls" if os.name == "nt" else "clear")
            # Salimos del bucle (retornamos)
            return
        
        # Si la opción no es válida
        else:
            # Mostramos mensaje de error
            mostrar_opcion_invalida()
            # Esperamos a que el usuario presione Enter
            input("Presione Enter...")
