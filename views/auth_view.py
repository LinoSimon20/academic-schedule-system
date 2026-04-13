def limpiar_pantalla():
    print("\n" * 20)


def mostrar_menu_inicial():
    print("Bienvenido al sistema de horarios")
    print("1. Iniciar sesión")
    print("2. Crear una cuenta")


def solicitar_credenciales():
    nombre = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    return nombre, password


def solicitar_nuevo_usuario():
    nombre = input("Ingrese un nombre de usuario: ").strip()
    password = input("Ingrese una contraseña: ").strip()
    password1 = input("Ingrese nuevamente la contraseña: ").strip()
    return nombre, password, password1


def mostrar_error(mensaje):
    print(f"Error: {mensaje}")


def mostrar_exito(mensaje):
    print(f"Éxito: {mensaje}")
