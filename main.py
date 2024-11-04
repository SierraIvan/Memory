import random
from colorama import Fore, Style, init


# Función para crear el tablero con emojis y el tablero oculto
def crear_tablero(filas, columnas):
    lista_emotes = ["🤣", "😉", "😍", "😘", "🤑", "🥵", "🤔", "😎", "😲", "😭", "😞", "😴", "🤒", "🤢", "🥶"]
    lista = []
    num_pares = (filas * columnas) // 2

    # Generamos los pares de emojis
    for i in range(num_pares):
        lista.extend([lista_emotes[i], lista_emotes[i]])

    # Desordenamos la lista para que sea aleatorio
    random.shuffle(lista)

    # Transformamos la lista plana en un tablero 2D de acuerdo a las filas y columnas dadas
    tablero = [lista[i * columnas:(i + 1) * columnas] for i in range(filas)]
    tablero_oculto = [["-" for _ in range(columnas)] for _ in range(filas)]

    return tablero, tablero_oculto

def mostrartablero():
    for fila in tablero:
        for celda in fila:
            print(" ", celda, end=" ")
        print()  # Salto de línea al final de cada fila

def imprimir_tablero(tablero):
    for fila in tablero:
        for celda in fila:
            if isinstance(celda, int) and celda < 10:
                print(f"  {celda}", end=" ")
            else:
                print(f" {celda}", end=" ")
        print()

def jugadorvsjugador():
    Jugador1 = input("Introduce el nombre del Jugador 1: ")
    Jugador2 = input("Introduce el nombre del Jugador 2: ")
    player1_puntuacion = 0
    player2_puntuacion = 0
    jugador_actual = True
    partida = True
    while partida:
        if jugador_actual:
            print("Turno de ", Jugador1)
        else:
            print("Turno de ", Jugador2)
        
        print("\nTablero actual:")
        imprimir_tablero(tablero_oculto)
        fila_revelar1 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas ) + "): "))
        columna_revelar1 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): "))
        
        fila_revelar1 = fila_revelar1 - 1
        columna_revelar1 = columna_revelar1 -1 


        item1 = tablero[fila_revelar1][columna_revelar1]
        tablero_oculto[fila_revelar1][columna_revelar1] = item1


        print("\nTablero después de revelar la primera posición:")
        imprimir_tablero(tablero_oculto)


        fila_revelar2 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): "))
        columna_revelar2 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): "))
        
        fila_revelar2 = fila_revelar2 - 1
        columna_revelar2 =  columna_revelar2 -1
        
        item2 = tablero[fila_revelar2][columna_revelar2]
        tablero_oculto[fila_revelar2][columna_revelar2] = item2

        # Imprimir el tablero con ambas posiciones reveladas
        print("\nTablero después de revelar ambas posiciones:")
        imprimir_tablero(tablero_oculto)

        # Verificar si los dos items son iguales
        if item1 == item2:
            print("Felicidades, pareja encontrada")
            if jugador_actual:
                player1_puntuacion += 1
            else:
                player2_puntuacion += 1
        else:
            print("Has fallado, se cambia de turno.")
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = "-", "-"
            jugador_actual = not jugador_actual
                
        print(Jugador1, ": ", player1_puntuacion, "        ", Jugador2, ": ", player2_puntuacion)

       

        if player1_puntuacion + player2_puntuacion >= (filas * columnas) // 2 :

            print("Juego Terminado")

            if player1_puntuacion > player2_puntuacion:
                print("Felicidades ", Jugador1," has ganado con ", player1_puntuacion, "puntos")
            else:
                print("Felicidades ", Jugador2," has ganado con ", player2_puntuacion, "puntos")

            SN = input("¿Volver a jugar? S/N: ")
            if SN == "S":
                opcionjuego()
            else:
                print("Saliendo del juego...")
                break
        enter = input("\nPulsa Enter para continuar...")

def jugadorvscpu():
    Jugador = input("Introduce el nombre del Jugador: ")
    player_puntuacion = 0
    cpu_puntuacion = 0
    jugador_actual = True
    partida = True
    while partida:
        if jugador_actual:
            print("Turno de ", Jugador)
        else:
            print("Turno de la maquina")
        
        # Imprimir el tablero actual
        if jugador_actual:
            print("\nTablero actual:")
            imprimir_tablero(tablero_oculto)

            # Pedimos la primera posición que queremos revelar
            fila_revelar1 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas ) + "): "))
            columna_revelar1 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): "))
            
            fila_revelar1 = fila_revelar1 - 1
            columna_revelar1 = columna_revelar1 -1 


            item1 = tablero[fila_revelar1][columna_revelar1]
            tablero_oculto[fila_revelar1][columna_revelar1] = item1


            print("\nTablero después de revelar la primera posición:")
            imprimir_tablero(tablero_oculto)


            fila_revelar2 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): "))
            columna_revelar2 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): "))
            
            fila_revelar2 = fila_revelar2 - 1
            columna_revelar2 =  columna_revelar2 -1


            item2 = tablero[fila_revelar2 ][columna_revelar2]
            tablero_oculto[fila_revelar2][columna_revelar2] = item2


            print("\nTablero después de revelar ambas posiciones:")
            imprimir_tablero(tablero_oculto)

        if not jugador_actual:
            fila_revelar1 = random.randint(0,filas - 1)
            columna_revelar1 = random.randint(0,columnas - 1)
            
            item1 = tablero[fila_revelar1][columna_revelar1]
            tablero_oculto[fila_revelar1][columna_revelar1] = item1

            fila_revelar2 = random.randint(0,filas - 1)
            columna_revelar2 = random.randint(0,columnas - 1)
            
            item2 = tablero[fila_revelar2][columna_revelar2]
            tablero_oculto[fila_revelar2][columna_revelar2] = item2

            print("\nTablero después de revelar ambas posiciones:")
            imprimir_tablero(tablero_oculto)
            print("Se mostraron las cartas ", fila_revelar1 , "", columna_revelar1, " y ", fila_revelar2 ,"",columna_revelar2)
        # Verificar si los dos items son iguales
        if item1 == item2:
            print("Felicidades, pareja encontrada")
            if jugador_actual:
                player_puntuacion += 1
            else:
                cpu_puntuacion += 1
        else:
            print("Has fallado, se cambia de turno.")
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = "-", "-"
            jugador_actual = not jugador_actual
                
        print(Jugador, ": ", player_puntuacion, "        CPU : ", cpu_puntuacion)

        

        if player_puntuacion + cpu_puntuacion >= (filas * columnas) // 2 :
            print("Juego Terminado")

            if player_puntuacion > cpu_puntuacion:
                print("Felicidades ", Jugador," has ganado con ", player_puntuacion, "puntos")
            else:
                print("Has perdido")

            SN = input("¿Volver a jugar? S/N: ")
            if SN == "S":
                opcionjuego()
            else:
                print("Saliendo del juego...")
                break
        enter = input("\nPulsa Enter para continuar...")



def cpuvscpu():
    print("hola")

def reglas(): 
    print("\n\n")
    print("Las partidas son por turnos \nSi el jugador acierta una pareja en su truno, continua \nsi falla perdera el turno \n\nEl jugador que mas puntos tenga cuando se \ndescubra todo el tablero, ganara")

    SN =  input("¿Quieres jugar? S/N: ")
    if(SN == "S"):
        opcionjuego()

def opcionjuego():
    
# Inicializar colorama
    init(autoreset=True)

    # Crear el menú estilizado
    print(f"{Style.BRIGHT}{Fore.CYAN}{'=' * 40}")
    print(f"{Fore.GREEN}{Style.BRIGHT}      ** BIENVENIDO A MEMORY **")
    print(f"{Style.RESET_ALL}{Fore.CYAN}{'=' * 40}\n")

    # Opciones del menú
    print(f"{Fore.YELLOW}0 - {Style.BRIGHT}¿Cómo se juega?")
    print(f"{Fore.YELLOW}1 - {Style.BRIGHT}Jugador vs Jugador")
    print(f"{Fore.YELLOW}2 - {Style.BRIGHT}Jugador vs Máquina")
    print(f"{Fore.YELLOW}3 - {Style.BRIGHT}Máquina vs Máquina")
    print(f"{Fore.YELLOW}4 - {Style.BRIGHT}Salir")

    # Línea decorativa al final
    print(f"\n{Fore.CYAN}{'=' * 40}")
    opcion = int(input("que opcion eliges: "))
    while True:
        match opcion:
            case 0:
                reglas()
                break
            case 1: 
                jugadorvsjugador()
                break
            case 2:
                jugadorvscpu()
                break
            case 3:
                cpuvscpu()
                break
            case 4:
                print("Saliendo del juego...")
                break
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
                break


print("Bienvenido a Memory, vamos a crear el tablero lo primero")
# Solicitamos las dimensiones del tablero
filas = int(input("Dime cuántas filas quieres que tenga el tablero: "))
columnas = int(input("Dime cuántas columnas quieres que tenga el tablero: "))

# Verificamos que la multiplicación de filas y columnas sea par y no sea mayor a 5 x 6 
while (filas * columnas) % 2 != 0 or filas > 5 or columnas > 6:
    if filas > 5 or columnas > 6:
        print("Lo máximo permitido para el tablero es 5 x 6")
    else:
        print("La multiplicación de filas x columnas tiene que dar par")
    
    filas = int(input("Dime cuántas filas quieres que tenga el tablero: "))
    columnas = int(input("Dime cuántas columnas quieres que tenga el tablero: "))

# Crea ambos tableros
tablero, tablero_oculto = crear_tablero(filas, columnas)

# Selección de modo de juego
opcionjuego()
