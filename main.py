from controllers.auth_controller import menu_inicial
import os, time

# Funcion para verificar si el archivo de base de datos existe
def archivo_existe(directorio, nombre_archivo):
    ruta = os.path.join(directorio, nombre_archivo)
    return os.path.isfile(ruta)

# Funcion para asegurar que la base de datos exista antes de iniciar el programa
def asegurar_base_de_datos():
    ruta = os.path.join("database", "academic_schedule.db")

    # Verificamos si el directorio de base de datos existe, si no, lo creamos
    if not os.path.exists("database"):
        os.makedirs("database")

    # Verificamos si el archivo de base de datos existe
    if not os.path.isfile(ruta):
        print("No se encontró la base de datos en:", ruta)
        print("Creando base de datos...")
        from scripts.create_db import crear_base_de_datos
        try:
            crear_base_de_datos()
            print("Redireccionando al menú principal...")
            time.sleep(3)

        # Si ocurre un error al crear la base datos, informamos al usuario
        except Exception as e:
            print("Error al crear la base de datos:", e)
            print("Créala manualmente ejecutando 'python scripts/create_db.py'")

# Invocamos las funciones para asegurar y luego mostramos el menu de inicio se sesión
if __name__ == "__main__":
    asegurar_base_de_datos()
    menu_inicial()