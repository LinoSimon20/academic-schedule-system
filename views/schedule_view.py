# Función para mostrar la lista de materias disponibles en formato de tabla
def mostrar_materias_lista(materias):
    # Imprimimos el encabezado de la tabla
    print("=" * 50)
    print("MATERIAS DISPONIBLES")
    print("=" * 50)
    # Imprimimos los encabezados de columnas
    print(f"{'Sigla':<15} | {'Nombre':<30}")
    print("-" * 50)
    # Si no hay materias, mostramos un mensaje
    if not materias:
        print("No hay materias registradas.")
        print("=" * 50)
        return
    # Iteramos sobre cada materia y la mostramos en formato de tabla
    for sigla, nombre in materias:
        print(f"{sigla:<15} | {nombre:<30}")
    # Imprimimos línea final de la tabla
    print("=" * 50)

# Función para mostrar un mensaje confirmando que se agregó una materia
def mostrar_materia_agregada(sigla, nombre):
    # Imprimimos un mensaje de éxito con los detalles de la materia agregada
    print("=" * 50)
    print("✓ MATERIA AGREGADA")
    print("=" * 50)
    print(f"Sigla: {sigla}")
    print(f"Nombre: {nombre}")
    print("=" * 50)

# Función para mostrar un mensaje confirmando que se eliminó una materia
def mostrar_materia_eliminada(sigla):
    # Imprimimos un mensaje de éxito con la sigla de la materia eliminada
    print("=" * 50)
    print("✓ MATERIA ELIMINADA")
    print("=" * 50)
    print(f"Sigla: {sigla}")
    print("=" * 50)

# Función para mostrar un mensaje de error relacionado con materias
def mostrar_error_materia(mensaje):
    # Imprimimos un mensaje de error formateado
    print("=" * 50)
    print("✗ ERROR")
    print("=" * 50)
    print(f"Mensaje: {mensaje}")
    print("=" * 50)

# Función para mostrar la lista de días disponibles para seleccionar
def mostrar_dias(dias):
    # Imprimimos el encabezado de la lista de días
    print("\nDÍAS DISPONIBLES:")
    print("-" * 30)
    # Iteramos sobre cada día y lo mostramos con su identificador
    for id_dia, nombre_dia in dias:
        # Mostramos el id del día y su nombre para que el usuario pueda seleccionar
        print(f"{id_dia}. {nombre_dia}")

# Función para mostrar la lista de horas disponibles para seleccionar
def mostrar_horas(horas):
    # Imprimimos el encabezado de la lista de horas
    print("\nHORAS DISPONIBLES:")
    print("-" * 30)
    # Iteramos sobre cada hora y la mostramos con su identificador
    for id_hora, hora in horas:
        # Mostramos el id de la hora y la hora en formato HH:MM
        print(f"{id_hora}. {hora}")

# Función para mostrar la lista de materias disponibles para agregar al horario
def mostrar_materias_para_horario(materias):
    # Imprimimos el encabezado de la lista de materias
    print("\nMATERIAS DISPONIBLES:")
    print("-" * 50)
    # Iteramos sobre cada materia y la mostramos con su identificador
    for id_materia, sigla, nombre in materias:
        # Mostramos el id de la materia, sigla y nombre para que el usuario pueda seleccionar
        print(f"{id_materia}. {sigla:<15} - {nombre}")

# Función para mostrar el horario completo de un usuario
def mostrar_horario_usuario(horario):
    # Imprimimos el encabezado del horario
    print("\n" + "=" * 70)
    print("TU HORARIO ACADÉMICO")
    print("=" * 70)
    # Si el horario está vacío, mostramos un mensaje
    if not horario:
        print("No hay clases registradas en tu horario.")
        print("=" * 70)
        return
    # Mostramos los encabezados de columnas
    print(f"{'Sigla':<10} | {'Materia':<20} | {'Día':<12} | {'Hora':<8}")
    print("-" * 70)
    # Iteramos sobre cada entrada del horario y la mostramos
    for id_h, sigla, nombre, dia, hora in horario:
        # Mostramos la entrada del horario en formato de tabla
        print(f"{sigla:<10} | {nombre:<20} | {dia:<12} | {hora:<8}")
    # Imprimimos línea final de la tabla
    print("=" * 70)

# Función para mostrar un mensaje de éxito cuando se agrega un horario
def mostrar_horario_agregado():
    # Imprimimos un mensaje de éxito
    print("\n" + "=" * 50)
    print("✓ ENTRADA DE HORARIO AGREGADA EXITOSAMENTE")
    print("=" * 50)

# Función para mostrar un mensaje de éxito cuando se elimina un horario
def mostrar_horario_eliminado():
    # Imprimimos un mensaje de éxito
    print("\n" + "=" * 50)
    print("✓ ENTRADA DE HORARIO ELIMINADA EXITOSAMENTE")
    print("=" * 50)

# Función para mostrar un mensaje de error relacionado con horarios
def mostrar_error_horario(mensaje):
    # Imprimimos un mensaje de error formateado
    print("\n" + "=" * 50)
    print("✗ ERROR EN HORARIO")
    print("=" * 50)
    print(f"Mensaje: {mensaje}")
    print("=" * 50)

