# Vista para la autenticacion de usuarios
# Funcion para limpiar la pantalla (simulada con saltos de linea)
def limpiar_pantalla():
    print("\n" * 20)

# Funcione para mostrar el menu de incio de sesión
def mostrar_menu_inicial():
    print("Bienvenido al sistema de horarios")
    print("1. Iniciar sesión")
    print("2. Crear una cuenta")

# Funcion para solicitar los datos de inisio de sesión
def solicitar_credenciales():
    nombre = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    return nombre, password

# Funcion para solicitar los datos de registro de una nueva cuenta
def solicitar_nuevo_usuario():
    nombre = input("Ingrese un nombre de usuario: ").strip()
    password = input("Ingrese una contraseña: ").strip()
    password1 = input("Ingrese nuevamente la contraseña: ").strip()
    return nombre, password, password1

# Funcion para mostrar un mensanje de error al usuario
def mostrar_error(mensaje):
    print(f"Error: {mensaje}")

# Funcion para mostrar un mensaje de exito al usuario
def mostrar_exito(mensaje):
    print(f"Éxito: {mensaje}")
