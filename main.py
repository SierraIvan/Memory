#Imporatamos random
import random


Nombre = input("Introduce tu nombre: ")

filas = 0
columnas =0

fila = int(input("Dime cuantas filas quieres que tenga el tablero"))
columnas = int(input("Dime cuantas columnas quiere que tenga el tablero"))
while((filas * columnas) % 2 != 0):
    print("La multiplicacion de filas x columnas tiene que dar par")
    fila = int(input("Dime cuantas filas quieres que tenga el tablero"))
    columnas = int(input("Dime cuantas columnas quiere que tenga el tablero"))





# Rellenamos la tabla con nuemeros aleatorios del 1 al 15
lista = []
for i in range(1, 16):
    lista.extend([i, i])

# Desordenamos la lista
random.shuffle(lista)

tabla = [lista[i:i+columnas] for i in range(0, len(lista), columnas)]

listaOculta = lista


cont = 0
for i in range(len(listaOculta)):
    # Imprime tablero oculto
    print("-", end=" ") 
    cont += 1
    if cont == 5:
        cont = 0
        print()
        
for i in range(len(lista)):
    # Verificamos la longitud del número en `lista[i]` para agregar los espacios necesarios
    if lista[i] < 10:
        print("  ", lista[i], end=" ")
    else:
        print(" ", lista[i], end=" ")
    cont += 1
    if cont == 5:
        cont = 0
        print()


