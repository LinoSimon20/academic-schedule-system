# Función para limpiar la pantalla mostrando múltiples saltos de línea
def limpiar_pantalla():
    # Imprimimos 20 saltos de línea para simular una pantalla limpia
    print("\n" * 20)

# Función para mostrar el menú de inicio de sesión o registro
def mostrar_menu_inicial():
    # Imprimimos el título del sistema
    print("=" * 50)
    print("SISTEMA DE GESTIÓN DE HORARIOS ACADÉMICOS")
    print("=" * 50)
    # Imprimimos las opciones disponibles
    print("\n1. Iniciar sesión")
    print("2. Crear una cuenta")
    print("-" * 50)

# Función para solicitar las credenciales de acceso al usuario
def solicitar_credenciales():
    # Solicitamos el nombre de usuario
    nombre = input("Usuario: ").strip()
    # Solicitamos la contraseña
    password = input("Contraseña: ").strip()
    # Retornamos ambas credenciales como tupla
    return nombre, password

# Función para solicitar los datos necesarios para crear una nueva cuenta
def solicitar_nuevo_usuario():
    # Solicitamos el nombre del nuevo usuario
    nombre = input("Ingrese un nombre de usuario: ").strip()
    # Solicitamos la contraseña del nuevo usuario
    password = input("Ingrese una contraseña: ").strip()
    # Solicitamos la confirmación de la contraseña
    password1 = input("Ingrese nuevamente la contraseña: ").strip()
    # Retornamos los datos como tupla
    return nombre, password, password1

# Función para mostrar un mensaje de error al usuario
def mostrar_error(mensaje):
    # Imprimimos el mensaje de error formateado
    print(f"\n✗ Error: {mensaje}")

# Función para mostrar un mensaje de éxito al usuario
def mostrar_exito(mensaje):
    # Imprimimos el mensaje de éxito formateado
    print(f"\n✓ Éxito: {mensaje}")

