import os
import time
from models.user import buscar_usuario, crear_usuario, existe_usuario
from views.auth_view import (
    solicitar_credenciales,
    solicitar_nuevo_usuario,
    mostrar_error,
    mostrar_exito,
    mostrar_menu_inicial,
    limpiar_pantalla,
)


def verificar_usuario(nombre, password):
    return buscar_usuario(nombre, password)


def iniciar_sesion():
    while True:
        limpiar_pantalla()
        mostrar_menu_inicial()
        nombre, password = solicitar_credenciales()
        usuario = verificar_usuario(nombre, password)
        if usuario:
            limpiar_pantalla()
            from controllers.menu_controller import mostrar_menu
            mostrar_menu(usuario)
            break
        mostrar_error("Credenciales inválidas. Intente nuevamente.")
        time.sleep(2)


def crear_usuario_interactivo():
    limpiar_pantalla()
    nombre, password, password1 = solicitar_nuevo_usuario()

    if not nombre or not password:
        mostrar_error("El nombre de usuario y la contraseña no pueden estar vacíos.")
        return

    if password != password1:
        mostrar_error("Las contraseñas no coinciden.")
        return

    if existe_usuario(nombre):
        mostrar_error("El usuario ya existe.")
        return

    crear_usuario(nombre, password)
    mostrar_exito("Usuario creado exitosamente. Por favor, inicie sesión.")


def menu_inicial():
    while True:
        limpiar_pantalla()
        mostrar_menu_inicial()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            iniciar_sesion()
            break
        elif opcion == "2":
            crear_usuario_interactivo()
            input("Presione Enter para continuar...")
        else:
            mostrar_error("Opción inválida. Por favor, seleccione 1 o 2.")
            time.sleep(1)
