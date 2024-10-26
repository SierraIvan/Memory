#Imporatamos random
import random


Nombre = input("Introduce tu nombre: ")

# Solicitamos las dimensiones del tablero
filas = int(input("Dime cuántas filas quieres que tenga el tablero: "))
columnas = int(input("Dime cuántas columnas quieres que tenga el tablero: "))


# Verificamos que la multiplicación de filas y columnas sea par y no sea mayor a 5 x 6 
while (filas * columnas) % 2 != 0 or filas > 5 or columnas > 6:
    if filas > 6 or columnas > 6:
        print("Lo máximo permitido para el tablero es 5 x 6")
    else:
        print("La multiplicación de filas x columnas tiene que dar par")
    
    filas = int(input("Dime cuántas filas quieres que tenga el tablero: "))
    columnas = int(input("Dime cuántas columnas quieres que tenga el tablero: "))





lista = []
num_pares = (filas * columnas) // 2  # La cantidad de pares necesarios
for i in range(1, num_pares + 1):
    lista.extend([i, i])

# Desordenamos la lista
random.shuffle(lista)

listaOculta = lista.copy()

cont = 0
for i in range(len(listaOculta)):
    # Imprime tablero oculto
    print("-", end=" ") 
    cont += 1
    if cont == columnas:
        cont = 0
        print()

print()   
for i in range(len(lista)):
    # Verificamos la longitud del número en `lista[i]` para agregar los espacios necesarios
    if lista[i] < 10:
        print("  ", lista[i], end=" ")
    else:
        print(" ", lista[i], end=" ")
    cont += 1
    if cont == columnas:
        cont = 0
        print()


