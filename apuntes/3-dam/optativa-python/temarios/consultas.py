import sqlite3

def realizar_consultas():
    # Establezco la conexión con la base de datos que ya he creado
    conn = sqlite3.connect("biblioteca.db")

    # Configuración clave: hago que las filas se comporten como diccionarios
    # para poder acceder a los datos por nombre de columna
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()

    # a) Mostrar todos los libros
    print("\n *** Todos los libros ***")
    cursor.execute("SELECT * FROM libros")
    # Recorro cada fila y accedo a los datos por el nombre de la columna
    for libro in cursor.fetchall():
        print(f"Título: {libro['titulo']} --- Autor: {libro['autor']} --- Año: {libro['anio']}")

    # b) Mostrar los socios mayores de edad (edad >= 18)
    print("\n *** Socios mayores de edad ***")
    cursor.execute("SELECT * FROM socios WHERE edad >= 18")
    for socio in cursor.fetchall():
        print(f"Nombre: {socio['nombre']} --- Edad: {socio['edad']}")

    # c) Mostrar préstamos de más de 7 días
    print ("\n *** Prestamos de más de 7 días ***")
    cursor.execute("SELECT * FROM prestamos WHERE dias_prestamo > 7")
    # Como es una lista de objetos, debo recorrerla para mostrar cada campo
    for p in cursor.fetchall():
        print(f"ID Préstamo: {p['id']} | Libro ID: {p['libro_id']} | Días: {p['dias_prestamo']}")

    # d) Mostrar el nombre del socio y el título del libro prestado (usando JOIN)
    print("\n *** Nombre del socio y título del libro prestado ***")
    query = """
        SELECT socios.nombre as nombre_socio, libros.titulo as titulo_libro
        FROM prestamos
        JOIN socios ON prestamos.socio_id = socios.id
        JOIN libros ON prestamos.libro_id = libros.id
        """
    cursor.execute(query)
    # Aquí accedo a los alias que he definido en la query (nombre_socio, titulo_libro)
    for fila in cursor.fetchall():
        print(f"Socio: {fila['nombre_socio']} --- Libro: {fila['titulo_libro']}")

    # e) Mostrar el primer préstamo registrado (fetchone)
    print("\n *** Primer préstamo registrado ***")
    cursor.execute("SELECT * FROM prestamos ORDER BY id ASC")
    # fetchone me devuelve un solo objeto, así que accedo a sus claves directamente
    primer_prestamo = cursor.fetchone()
    if primer_prestamo: # Verifico que haya datos para evitar errores
        print(f"ID: {primer_prestamo['id']} | Socio ID: {primer_prestamo['socio_id']} | Días: {primer_prestamo['dias_prestamo']}")

    # f) Mostrar cuántos préstamos hay en total
    print("\n *** Total de préstamos ***")
    cursor.execute("SELECT COUNT(*) FROM prestamos")
    # Fetchone me devuelve una tupla con un solo valor, por eso accedo al índice [0]
    total = cursor.fetchone()[0]
    print(f"Total de préstamos: {total}")

    # Cierro la conexión para liberar la base de datos
    conn.close()

if __name__ == "__main__":
    realizar_consultas()