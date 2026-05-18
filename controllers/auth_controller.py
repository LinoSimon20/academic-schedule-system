# Importamos el módulo os para limpiar la pantalla
import os
# Importamos el módulo time para hacer pausas
import time
# Importamos las funciones de modelo de usuario para autenticación
from models.user import buscar_usuario, crear_usuario, existe_usuario
# Importamos las funciones de vista para mostrar mensajes de autenticación
from views.auth_view import (
    solicitar_credenciales,
    solicitar_nuevo_usuario,
    mostrar_error,
    mostrar_exito,
    mostrar_menu_inicial,
    limpiar_pantalla,
)

# Función para verificar las credenciales de un usuario
def verificar_usuario(nombre, password):
    # Llamamos a la función buscar_usuario que retorna (id, nombre) si es válido o None
    return buscar_usuario(nombre, password)

# Función para gestionar el proceso de inicio de sesión
def iniciar_sesion():
    # Iniciamos un bucle infinito para permitir reintentos
    while True:
        # Limpiamos la pantalla
        limpiar_pantalla()
        # Mostramos el menú inicial con opciones de autenticación
        mostrar_menu_inicial()
        # Solicitamos las credenciales del usuario
        nombre, password = solicitar_credenciales()
        # Verificamos si las credenciales son válidas consultando la base de datos
        usuario = verificar_usuario(nombre, password)
        # Si el usuario existe (credenciales válidas)
        if usuario:
            # Limpiamos la pantalla
            limpiar_pantalla()
            # Importamos el menú principal para mostrar después de autenticarse
            from controllers.menu_controller import mostrar_menu
            # Mostramos el menú principal con el usuario autenticado
            mostrar_menu(usuario)
            # Salimos del bucle (sesión finalizada)
            break
        # Si las credenciales son inválidas, mostramos un mensaje de error
        mostrar_error("Credenciales inválidas. Intente nuevamente.")
        # Hacemos una pausa de 2 segundos antes de reintentar
        time.sleep(2)

# Función para crear un nuevo usuario interactivamente
def crear_usuario_interactivo():
    # Limpiamos la pantalla
    limpiar_pantalla()
    # Solicitamos los datos del nuevo usuario (nombre, contraseña y confirmación)
    nombre, password, password1 = solicitar_nuevo_usuario()

    # Verificamos que el nombre de usuario no esté vacío
    if not nombre or not password:
        # Si está vacío, mostramos un mensaje de error y retornamos
        mostrar_error("El nombre de usuario y la contraseña no pueden estar vacíos.")
        return

    # Verificamos que las dos contraseñas coincidan
    if password != password1:
        # Si no coinciden, mostramos un mensaje de error y retornamos
        mostrar_error("Las contraseñas no coinciden.")
        return

    # Verificamos que el usuario no exista ya en la base de datos
    if existe_usuario(nombre):
        # Si ya existe, mostramos un mensaje de error y retornamos
        mostrar_error("El usuario ya existe.")
        return

    # Creamos el nuevo usuario en la base de datos
    crear_usuario(nombre, password)
    # Mostramos un mensaje de éxito al usuario
    mostrar_exito("Usuario creado exitosamente. Por favor, inicie sesión.")

# Función para mostrar el menú inicial y gestionar la autenticación
def menu_inicial():
    # Iniciamos un bucle infinito para mantener el menú activo
    while True:
        # Limpiamos la pantalla
        limpiar_pantalla()
        # Mostramos el menú inicial con opciones
        mostrar_menu_inicial()
        # Solicitamos al usuario que seleccione una opción
        opcion = input("Seleccione una opción: ").strip()
        # Si selecciona opción 1, inicia sesión
        if opcion == "1":
            # Llamamos a la función para iniciar sesión
            iniciar_sesion()
            # Salimos del bucle (usuario autenticado)
            break
        # Si selecciona opción 2, crea una nueva cuenta
        elif opcion == "2":
            # Llamamos a la función para crear usuario interactivamente
            crear_usuario_interactivo()
            # Esperamos a que presione Enter para continuar
            input("Presione Enter para continuar...")
        # Si la opción no es válida
        else:
            # Mostramos un mensaje de error
            mostrar_error("Opción inválida. Por favor, seleccione 1 o 2.")
            # Hacemos una pausa de 1 segundo
            time.sleep(1)

