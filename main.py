# Importamos la función del controlador de autenticación para el menú inicial
from controllers.auth_controller import menu_inicial
# Importamos el módulo os para operaciones del sistema operativo
import os
# Importamos el módulo time para hacer pausas
import time

# Función para verificar si un archivo existe en una carpeta específica
def archivo_existe(directorio, nombre_archivo):
    # Construimos la ruta completa del archivo
    ruta = os.path.join(directorio, nombre_archivo)
    # Verificamos si el archivo existe como archivo (no carpeta)
    return os.path.isfile(ruta)

# Función para asegurar que la base de datos exista antes de iniciar el programa
def asegurar_base_de_datos():
    # Definimos la ruta donde debe estar la base de datos
    ruta = os.path.join("database", "academic_schedule.db")

    # Verificamos si el directorio de base de datos existe, si no, lo creamos
    if not os.path.exists("database"):
        # Creamos la carpeta database si no existe
        os.makedirs("database")

    # Verificamos si el archivo de base de datos existe
    if not os.path.isfile(ruta):
        # Informamos al usuario que no se encontró la base de datos
        print("No se encontró la base de datos en:", ruta)
        # Informamos que se va a crear
        print("Creando base de datos...")
        # Importamos la función para crear la base de datos
        from scripts.create_db import crear_base_de_datos
        try:
            # Ejecutamos la función para crear la base de datos con todas las tablas
            crear_base_de_datos()
            # Informamos que se redirige al menú principal
            print("Redireccionando al menú principal...")
            # Hacemos una pausa de 3 segundos
            time.sleep(3)

        # Si ocurre un error al crear la base datos, lo capturamos
        except Exception as e:
            # Informamos sobre el error
            print("Error al crear la base de datos:", e)
            # Sugerimos crear manualmente la base de datos
            print("Créala manualmente ejecutando 'python scripts/create_db.py'")

# Punto de entrada del programa (se ejecuta cuando se corre como script principal)
if __name__ == "__main__":
    # Primero nos aseguramos de que la base de datos existe
    asegurar_base_de_datos()
    # Luego mostramos el menú inicial de autenticación
    menu_inicial()
