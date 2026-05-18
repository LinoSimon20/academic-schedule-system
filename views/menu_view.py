# Función para mostrar un mensaje de bienvenida personalizado con el nombre del usuario
def mostrar_bienvenida(usuario):
    # Imprimimos un saludo personalizado con el nombre del usuario (usuario[1] es el nombre)
    print("\n" + "=" * 50)
    print(f"¡Bienvenido/a al sistema de horarios, {usuario[1]}!")
    print("=" * 50)

# Función para mostrar el menú principal con todas las opciones disponibles
def mostrar_menu_principal():
    # Imprimimos el título del menú
    print("\nMENÚ PRINCIPAL")
    print("-" * 50)
    # Imprimimos las opciones disponibles para el usuario
    print("1. Ver materias")
    print("2. Agregar materia")
    print("3. Eliminar materia")
    print("4. Crear horario")
    print("5. Consultar horario")
    print("6. Salir")
    print("-" * 50)

# Función para mostrar un mensaje cuando el usuario ingresa una opción inválida
def mostrar_opcion_invalida():
    # Imprimimos un mensaje de error para opción inválida
    print("\n✗ Opción inválida. Por favor seleccione una opción correcta.")

