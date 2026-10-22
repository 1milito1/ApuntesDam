#parte 1 Asignaciones y control de flujo.

#asisgnaciones múltiples y Slicing
#Declaro las 3 variabels y mostramos la suma en la terminal 

print(f"\n------Asignaciones múltiples-------")
a, b, c = 10, 20, 30
print(f"Los valores de la variable son: a={a}, b={b}, c={c}")
print(f"La suma de las variables es: {a+b+c}")



print(f"\n------Slicing-------")
 #Lista principal.
lista=[1, 2, 3, 4, 5]

#Descomposición de la lista en primero intermedio y ultimo para 
#recoger los resultados
primero, *intermedio, utltimo = lista

#Impresión de los resultados
print(f"\nLista principal: {lista}")
print(f"Primer número: {primero}")
print(f"Números intermedios: {intermedio}")
print(f"Último número: {utltimo}")


print(f"\n -------Control del flujo condicional-------")
#Hacemos un programa que pide al usuario un número y vemos si es mayor
#  o menor a 10 y su excepcion

try:
    numero = int(input("\nIntroduce un numero: "))
    if numero > 10:
        print("El número es mayor de 10")
    elif numero==10:
        print("El número es igual a 10")
    else:
        print("El número es menor a 10")
except ValueError:
    print("Número no válido. Por favor introduce un número entero.")



# Menú interactivo con match/case
import datetime
import random

#Variable para la fecha actual
fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y") #formato dia-mes-año

#Menú
opcion=0
while opcion != 3: #sigue siempre que la opcion no sea 3
    print("\n---Menú de opciones: ---")
    print ("1. Mostrar la fecha actual.")
    print("2. Generar número aleatorio.")
    print("3. Salir.")

    entrada = input("Elige una opción: ")

    try:
        opcion = int(entrada)
    except ValueError:
        opcion = 0 #Nos aseguramos que el case 0 entre si no es un número

    match opcion:
        case 1: 
            print(f"\nFecha actual: {fecha_actual}")
        case 2:
            numero = random.randint(1, 100)
            print(f"\nNúmero aleatorio: {numero}")
        case 3:
            print("\nCerrando el programa")
        case _:
            print("\nOpción no válida elige otra")


#Ejercicio de While
print("\n ----Bucle While ----")
suma=0
numero_ingresado = -1

while numero_ingresado != 0:
    try:
        entrada = input("Introduce un número para sumar (para salir 0): ")
        numero_ingresado = int(entrada)
        suma += numero_ingresado
    except ValueError:
        print("Entrada no váliad. Introduce un número entero.")
print(f"\nLa suma de todos los número es: {suma}")


#Ejercicio bucle for

print(f"\n ---- Bucle for con break y continue ----")
for numero in range(1, 21):
    if numero > 15:
        print(f"Numero {numero} es mayor de 15. Deteniendo bucle con break")
        break
    if numero % 3 == 0:
        print(f"Numero {numero} es divisible entre 3. Saltando la interación con continue")

    
    print(f"Núimero procesado {numero}")


#Función para vereficar si un número es primo
def es_primo(numero_entero: int)-> bool:
    if numero_entero < 2:
        return False
    for i in range(2, int(numero_entero ** 0.5) + 1):
        if numero_entero % i ==0:
            return False
    return True

print("\n --- Función número primo ---")
print(f"¿11 es primo? {es_primo(11)}")
print(f"¿15 es primo? {es_primo(15)}")
print(f"¿1 es primo? {es_primo(1)}")
print(f"¿2 es primo? {es_primo(2)}")


#Duplicar valores en lista
def ducplicar_lista(lista_principal: list) -> list:
    
    lista_duplicada = [x + 2 for x in lista_principal]
    return lista_duplicada
lista_entrada = [1, 2, 3, 4]
lista_salida=ducplicar_lista(lista_entrada)

print("\n --- Función duplicar lista ---")
print(f"Lista original: {lista_entrada}")
print(f"Lista duplicada: {lista_salida}")


#Función recursiva
def factorial_recursivo(n: int) -> int:
        
    if n <=1:
        return 1
    else:
        return n + factorial_recursivo(n - 1)

print(f"\n ---- Función factorial recursivo ----")
print(f"Factorial de 5: {factorial_recursivo(5)}")
print(f"Factorial de 0: {factorial_recursivo(0)}")
print(f"Factorial de 1: {factorial_recursivo(1)}")


#Invertir cadena de texto con función recursiva.
def invertir_cadena_recursiva(cadena: str) -> str:
    if len(cadena)<=1:
        return cadena
    else:
        return cadena[-1] + invertir_cadena_recursiva(cadena[:-1])
    
print(f"\n ---- Función invertir cadena recursiva ----")
cadena_entrada= "melocotón"
cadena_salida = invertir_cadena_recursiva(cadena_entrada)
print(f"Cadena original: {cadena_entrada}")
print(f"Cadena invertida: {cadena_salida}")


#Lambda para tuplas.
lista_tuplas = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (0, 'e')]
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])

print (f"\n---- Lambda para odenar tuplas ----")
print(f"Lista original: {lista_tuplas}")
print(f"Lista ordenada por el elemento segundo: {lista_ordenada}")



#Función de orden superior.

def cubo(x):
    #Función que cálcula el cubo de un número
    return x**3

def aplicar_función(lista: list, funcion_a_aplicar) -> list:
    #Función de orden superior que aplica la función a cada elemento de la 'lista'
    # y devuelve los resultados en una nueva lista 
    resultados = list(map(funcion_a_aplicar, lista))
    return resultados

numeros = [1, 2, 3, 4]
lista_cubos = aplicar_función(numeros, cubo)

print(f"\n---- Función de orden superior ----")
print(f"Lista original: {numeros}")
print(f"Lista de cubos: {lista_cubos}")


#Manejo de excepciones

class NumeroNegativoError(ValueError):
    #Excepción personalizada

    def __init__(self, numero, mensaje= "El número introducido no puede ser negativo. "):
        self.numero = numero
        self.mensaje = mensaje
        super().__int__(self.mensaje)

print("\n ---- Manejo de excepciones ----")

while True:
    try:
        entrada = input("Introduce un número entero: ")
        numero = int(entrada)

        if numero < 0:
            raise NumeroNegativoError(numero)
        print(f"Numero válido introducido: {numero}")
        break

    except ValueError as e:
        if isinstance(e, NumeroNegativoError):
            print("ERROR PERSONALIZADO: {e.mensaje} (Valor: {e.numero})")
        else:
            print("ERROR: Por favor, introduce un número entero válido.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

        


#Excepción propia

class IndiceFueraDeRangoError(IndexError):

    def __init__(self, indice, longitud, mensaje="intento de acceso a índice fuera de rango."):
        self.indice = indice
        self.longitud = longitud
        self.mensaje= f"{mensaje} Indice: {indice}, Longitud de la lista: {longitud}"
        super().__init__(self.mensaje)

    
def obener_elemento_con_validacion(lista: list, indice: int):
    longitud = len(lista)
    #Comprobar si el indice está dentro del rango válido
    if not(-longitud <= indice < longitud):
        #si no existe inciar la excepcion propia
        raise IndiceFueraDeRangoError(indice, longitud)
    else:
        #devuelve el elento en el indice si es válido
        return lista[indice]
    

print("\n ---- Excepción propia ----")
lista_ejemplo = ['a', 'b', 'c', 'd', 'e']
try:
    elemento_valido = obener_elemento_con_validacion(lista_ejemplo, 2)
    print (f"Elemento en índice 2: {elemento_valido}")
    elemento_fuera_de_rango = obener_elemento_con_validacion(lista_ejemplo, 10)
   
    #caso de indice fuera de rango lanza la excepción propia
    obener_elemento_con_validacion(lista_ejemplo, 5)
except IndiceFueraDeRangoError as e:
    print(f"ERROR PERSONALIZADO: {e.mensaje}")
    print(f"Detalles: Indice solicitado: {e.indice}, tamaño de la lista {e.longitud}")


#otro caso con un indice negativo fuera de rango 
try:
    obener_elemento_con_validacion(lista_ejemplo, -6)
except IndiceFueraDeRangoError as e:
    print(f"\n ERROR PERSONALIZADO: {e.mensaje}")
    


#Pirámide centrada.

print("\n ---- Pirámide centrada ----")
def dibujar_piramide(filas: int):

    for altura in range(1, numero_filas +1):
        espacios = numero_filas - altura
        for _ in range(espacios):
            print(" ", end= "")
        for j in range(1, altura +1):
            print(str(j), end="")
        for k in range(altura -1, 0, -1):
            print(str(k), end="")
        print()

        

try:
    filas = input ("introduce un número de filas: ")
    numero_filas = int (filas)
    print(f"Pirámide con {numero_filas} filas:")
    dibujar_piramide(numero_filas)
except ValueError as e:
    print("Número introducido no válido.") 