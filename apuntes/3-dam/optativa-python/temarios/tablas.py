import sqlite3

def crear_base_de_datos():
    #Creo la conexión a la base de datos
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    # Para evitar errores, elimino las tablas si ya existen
    cursor.execute("DROP TABLE IF EXISTS prestamos")
    cursor.execute("DROP TABLE IF EXISTS libros")
    cursor.execute("DROP TABLE IF EXISTS socios")

    # Creo la tabla libros
    cursor.execute("""
                   CREATE TABLE libros(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT,
                   autor TEXT,
                   anio INTEGER
                   )
                   """)
    
    # creo la tabla socios
    cursor.execute("""
                   CREATE TABLE socios(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   edad INTEGER
                   )
                   """)
    
    # creo la tabla prestamos
    cursor.execute("""
                    CREATE TABLE prestamos(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   libro_id INTEGER,
                   socio_id INTEGER,
                   dias_prestamo INTEGER,
                   FOREIGN KEY (libro_id) REFERENCES libros(id),
                   FOREIGN KEY (socio_id) REFERENCES socios(id)
                   )
                   """)
    
    # Guardo los cambios y cierro la conexión
    conn.commit()
    conn.close()
    print("Base de datos creada correctamente.")


if __name__ == "__main__":
    crear_base_de_datos()
