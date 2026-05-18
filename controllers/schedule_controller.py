# Importamos la función para obtener materias del modelo subject
from models.subject import obtener_materias, insertar_materia, eliminar_materia
# Importamos las funciones para gestionar horarios del modelo schedule
from models.schedule import (
    obtener_dias, 
    obtener_horas, 
    obtener_materias_para_horario,
    agregar_entrada_horario, 
    obtener_horario_usuario, 
    eliminar_entrada_horario,
    existe_entrada_horario
)
# Importamos las funciones de vista para mostrar materias y horarios
from views.schedule_view import (
    mostrar_materias_lista,
    mostrar_materia_agregada,
    mostrar_materia_eliminada,
    mostrar_error_materia,
    mostrar_dias,
    mostrar_horas,
    mostrar_materias_para_horario,
    mostrar_horario_usuario,
    mostrar_horario_agregado,
    mostrar_horario_eliminado,
    mostrar_error_horario,
)

# Función para mostrar todas las materias registradas en el sistema
def mostrar_materias():
    # Obtenemos la lista de todas las materias de la base de datos
    materias = obtener_materias()
    # Mostramos las materias en la vista
    mostrar_materias_lista(materias)

# Función para agregar una nueva materia al sistema
def agregar_materia():
    # Solicitamos al usuario la sigla de la materia
    sigla = input("Ingrese la sigla de la materia: ").strip()
    # Solicitamos al usuario el nombre completo de la materia
    nombre = input("Ingrese el nombre de la materia: ").strip()
    # Verificamos que ambos campos no estén vacíos
    if not sigla or not nombre:
        # Si alguno está vacío, mostramos error y retornamos
        mostrar_error_materia("La sigla y el nombre son obligatorios.")
        return
    # Intentamos insertar la materia en la base de datos
    if insertar_materia(sigla, nombre):
        # Si se insertó exitosamente, mostramos mensaje de éxito
        mostrar_materia_agregada(sigla, nombre)
    else:
        # Si hubo error, mostramos mensaje de error
        mostrar_error_materia("No se pudo agregar la materia. Verifique los datos.")

# Función para eliminar una materia del sistema
def eliminar_materia():
    # Solicitamos al usuario la sigla de la materia a eliminar
    sigla = input("Ingrese la sigla de la materia a eliminar: ").strip()
    # Verificamos que el campo no esté vacío
    if not sigla:
        # Si está vacío, mostramos error y retornamos
        mostrar_error_materia("La sigla es obligatoria.")
        return
    # Intentamos eliminar la materia de la base de datos
    if eliminar_materia(sigla):
        # Si se eliminó exitosamente, mostramos mensaje de éxito
        mostrar_materia_eliminada(sigla)
    else:
        # Si no se encontró la materia, mostramos mensaje de error
        mostrar_error_materia("No se encontró la materia con esa sigla.")

# Función para crear una nueva entrada en el horario del usuario actual
def crear_horario(id_usuario):
    try:
        # Obtenemos la lista de días disponibles de la base de datos
        dias = obtener_dias()
        # Verificamos que existan días registrados
        if not dias:
            # Si no hay días, mostramos error y retornamos
            mostrar_error_horario("No hay días registrados en el sistema.")
            return
        
        # Mostramos los días disponibles al usuario
        mostrar_dias(dias)
        # Solicitamos al usuario que seleccione un día
        id_dia_seleccionado = input("\nSeleccione el número del día: ").strip()
        
        # Obtenemos la lista de horas disponibles de la base de datos
        horas = obtener_horas()
        # Verificamos que existan horas registradas
        if not horas:
            # Si no hay horas, mostramos error y retornamos
            mostrar_error_horario("No hay horas registradas en el sistema.")
            return
        
        # Mostramos las horas disponibles al usuario
        mostrar_horas(horas)
        # Solicitamos al usuario que seleccione una hora
        id_hora_seleccionado = input("Seleccione el número de la hora: ").strip()
        
        # Obtenemos la lista de materias disponibles de la base de datos
        materias = obtener_materias_para_horario()
        # Verificamos que existan materias registradas
        if not materias:
            # Si no hay materias, mostramos error y retornamos
            mostrar_error_horario("No hay materias registradas en el sistema.")
            return
        
        # Mostramos las materias disponibles al usuario
        mostrar_materias_para_horario(materias)
        # Solicitamos al usuario que seleccione una materia
        id_materia_seleccionado = input("Seleccione el número de la materia: ").strip()
        
        # Convertimos los valores ingresados a enteros para validación
        try:
            # Convertimos el id del día a entero
            id_dia = int(id_dia_seleccionado)
            # Convertimos el id de la hora a entero
            id_hora = int(id_hora_seleccionado)
            # Convertimos el id de la materia a entero
            id_materia = int(id_materia_seleccionado)
        except ValueError:
            # Si la conversión falla, mostramos error y retornamos
            mostrar_error_horario("Los valores ingresados no son válidos.")
            return
        
        # Verificamos que la entrada de horario no exista ya
        if existe_entrada_horario(id_usuario, id_materia, id_dia, id_hora):
            # Si ya existe, mostramos error y retornamos
            mostrar_error_horario("Esta entrada de horario ya existe.")
            return
        
        # Intentamos agregar la nueva entrada al horario del usuario
        if agregar_entrada_horario(id_usuario, id_materia, id_dia, id_hora):
            # Si se agregó exitosamente, mostramos mensaje de éxito
            mostrar_horario_agregado()
        else:
            # Si hubo error, mostramos mensaje de error
            mostrar_error_horario("No se pudo agregar la entrada de horario.")
    
    except Exception as e:
        # Si ocurre cualquier excepción, la capturamos y mostramos error
        mostrar_error_horario(f"Error inesperado: {str(e)}")

# Función para consultar y mostrar el horario actual del usuario
def consultar_horario(id_usuario):
    try:
        # Obtenemos el horario completo del usuario de la base de datos
        horario = obtener_horario_usuario(id_usuario)
        # Mostramos el horario del usuario en la vista
        mostrar_horario_usuario(horario)
        # Si hay entradas en el horario, ofrecemos la opción de eliminar una
        if horario:
            # Preguntamos si desea eliminar una entrada
            eliminar = input("\n¿Desea eliminar alguna entrada? (s/n): ").strip().lower()
            # Si responde afirmativamente, ejecutamos la función de eliminación
            if eliminar == 's':
                # Ejecutamos la función para eliminar una entrada del horario
                eliminar_entrada_horario_usuario(horario)
    except Exception as e:
        # Si ocurre cualquier excepción, la capturamos y mostramos error
        mostrar_error_horario(f"Error al consultar horario: {str(e)}")

# Función auxiliar para eliminar una entrada específica del horario del usuario
def eliminar_entrada_horario_usuario(horario):
    try:
        # Solicitamos el identificador de la entrada a eliminar
        id_entrada = input("Ingrese el número de la entrada a eliminar: ").strip()
        # Convertimos el id a entero
        id_entrada = int(id_entrada)
        # Intentamos eliminar la entrada de la base de datos
        if eliminar_entrada_horario(id_entrada):
            # Si se eliminó exitosamente, mostramos mensaje de éxito
            mostrar_horario_eliminado()
        else:
            # Si no se encontró la entrada, mostramos mensaje de error
            mostrar_error_horario("No se encontró la entrada de horario a eliminar.")
    except ValueError:
        # Si la conversión a entero falla, mostramos error
        mostrar_error_horario("El valor ingresado no es válido.")
    except Exception as e:
        # Si ocurre cualquier excepción, la capturamos y mostramos error
        mostrar_error_horario(f"Error al eliminar entrada: {str(e)}")

