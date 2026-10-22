import sqlite3

# para insertar de forma eficiente voy a utilizar executemany

def insertar_datos():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    # Datos a insertar
    libros = [
        ("1984", "Orwell", 1949), 
        ("El Quijote", "Cervantes", 1605), 
        ("Dune", "Herbert", 1965),
        ("Cien años de soledad", "García Márquez", 1967),
        ("La sombra del viento", "Zafón", 2001)
    ]
    
    socios = [
        ("Ana", 20), 
        ("Luis", 17), 
        ("Marta", 25),
        ("Carlos", 30),
        ("Lucía", 19)
    ]
    
    prestamos = [
        (1, 1, 10), 
        (2, 3, 5),  
        (3, 1, 15), 
        (1, 2, 7),  
        (4, 4, 12), 
        (5, 5, 20)  
    ]

    # Inserto los datos
    cursor.executemany("INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)", libros)
    cursor.executemany("INSERT INTO socios (nombre, edad) VALUES (?, ?)", socios)
    cursor.executemany("INSERT INTO prestamos (libro_id, socio_id, dias_prestamo) VALUES (?, ?, ?)", prestamos)

    conn.commit()
    conn.close()
    print("Datos insertados")

if __name__ == "__main__":
    insertar_datos()