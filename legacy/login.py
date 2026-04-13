import connection_db, os, main_menu, time
print("Iniciando el programa...")

# Verificar usuario
def verificar_usuario(nombre, password):
    conn = connection_db.obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT id_usuario, nombre
                   FROM usuarios
                   WHERE nombre = ? AND password = ?
                   """, (nombre, password))
    usuario=cursor.fetchone()
    conn.close()
    return usuario

# Iniciar sesión
def iniciar_sesion():
    while True:
        print("Ingrese sus credenciales")
        nombre = input("Usuario: ")
        password = input("Contraseña: ")
        usuario = verificar_usuario(nombre, password)
        if usuario:
            os.system("cls")
            main_menu.mostrar_menu(usuario)
            break
        else:
            print("Credenciales inválidas. Intente nuevamente.")
            time.sleep(2)
            os.system("cls")

# Crear usuario
def crear_usuario():
    print("No se encontraron usuarios. Por favor, cree una cuenta.")
    nombre = input("Ingrese un nombre de usuario: ").strip()
    password = input("Ingrese una contraseña: ").strip()
    password1 = input("Ingrese nuevamente la contraseña: ").strip()
    if not nombre or not password:
        print("El nombre de usuario y la contraseña no pueden estar vacíos.")
        return
    if password != password1:
        print("Las contraseñas no coinciden.")
        return
    conn = connection_db.obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
    if cursor.fetchone():
        print("El usuario ya existe.")
        conn.close()
        return
    cursor.execute("""
                   INSERT INTO usuarios (nombre, password, id_tipo, id_carrera, id_mencion)
                   VALUES (?, ?, ?, ?, ?)
                   """, (nombre, password, 2, 1, 1))
    conn.commit()
    conn.close()
    print("Usuario creado exitosamente. Por favor, inicie sesión.")

# Menú inicial
def menu_inicial():
    while True:        
        print("¿Desea iniciar sesión (1) o crear una cuenta (2)?")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            iniciar_sesion()
            break
        elif opcion == "2":
            crear_usuario()
            break     
        else:           
            print("Opción inválida. Por favor, seleccione 1 o 2.")