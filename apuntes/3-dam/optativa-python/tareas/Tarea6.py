import csv
from pathlib import Path

# Ejercicio 1: leer el fichero .txt y devolver una lista de tuplas
def leer_empleados(ruta):
    empleados = []
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                if len(linea.strip()) == 0: continue
                idx = linea [0:3].strip()
                nombre = linea[3:13].strip()
                apellido = linea[13:23].strip()
                salario = int(linea[23:28].strip())

                empleados.append((idx, nombre, apellido, salario))
    except FileNotFoundError:
        print(f"El fichero {ruta} no existe")
    
    return empleados

# Ejercicio2: agregar un empleado al fichero respetando el ancho fijo
def agregar_empleado(ruta, empleado):
    idx, nom, ape, sal = empleado

    with open(ruta, 'a', encoding = 'utf-8') as f:
        linea = f"{idx:<3}{nom:<10}{ape:<10}{sal:>5}\n"
        f.write(linea)


# Ejercicio 3: calcular el salario medio de los empleados.
def salario_medio(empleados):
    if not empleados:
        return 0
    total_salario = sum(emp[3] for emp in empleados)
    return total_salario / len(empleados)


# Ejercicio 4: exportar a csv
def exportar_csv(ruta_salida, empleados):
    with open(ruta_salida, 'w', newline='', encoding='utf-8')as f:
        escritor = csv.writer(f)
        escritor.writerow(['Id', 'Nombre', 'Apellido', 'Salario'])
        escritor.writerows(empleados)



# Programa principal para pruebas con menú por terminal
def mostrar_menu():
    print("\n **** Gestión de empleados (Tarea6) ****")
    print("1. Leer empleados desde el archivo")
    print ("2. Agregar un nuevo empleado")
    print("3. Calcular salario medio de los empleados")
    print("4. Exportar a CSV")
    print("5. Salir")
    return input("Seleccione una opción: ")

import os
if __name__ == "__main__":
    # Al principio no me leía el archivo asi que decidí usar la ruta absoluta del script para asegurarme de que se encuentra el 
    # archivo empleados.txt en el mismo directorio que el programa
    ruta_script= os.path.dirname(os.path.abspath(__file__))
    archivo_txt = os.path.join(ruta_script, "empleados.txt")
    archivo_csv = os.path.join(ruta_script, "empleados.csv")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            lista = leer_empleados(archivo_txt)
            print("\n ID   | Nombre    | Apellido    | Salario")
            print("-" *40)
            for e in lista: 
                print(f"{e[0]:<4}| {e[1]:<11}| {e[2]:<11}| {e[3]}")
        elif opcion == "2":
            print("\n --- Ingrese los daatos del empleado ---")
            idx = input("ID (máx 3 caracteres): ")
            nom = input("Nombre ( máx. 10 caracteres): ")
            ape = input("Apellido (máx. 10 caracteres): ")
            try:
                sal = int(input("Salario (máx. 5 dígitos): "))
                agregar_empleado(archivo_txt, (idx, nom, ape, sal))
                print(f"empleado {nom} agregado exitosamente.")
            except ValueError:
                print("Error: el salario debe ser un número entero")
        elif opcion == "3":
            lista = leer_empleados(archivo_txt)
            media = salario_medio(lista)
            print (f"\n El salario medio es: {media:.2f}")
        elif opcion == "4":
            lista = leer_empleados(archivo_txt)
            if lista:
                exportar_csv(archivo_csv, lista)
                print(f"\n Empleados exportados a {archivo_csv}")
            else:
                print("No hay datos para exportar.")
        elif opcion == "5":
            print("Saliiendo del programa...")
            break
        else:
            print("Opcion no válida.")
