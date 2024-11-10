import random
from colorama import Fore, Style, init


#metodo para pedir como quiere que sea la tabla del juego
def pedir_dimensiones():
    while True:
        filas = int(input("Dime cuántas filas quieres que tenga el tablero: "))
        columnas = int(input("Dime cuántas columnas quieres que tenga el tablero: "))

        if (filas * columnas) % 2 == 0 and filas <= 5 and columnas <= 6:
            return filas, columnas
        else:
            if filas > 5 or columnas > 6:
                print("Lo máximo permitido para el tablero es 5 x 6.")
            else:
                print("La multiplicación de filas x columnas tiene que dar un número par.")



#metodo para crear la tabla con emgies
def crear_tablero(filas, columnas):
    lista_emotes = ["🤣", "😉", "😍", "😘", "🤑", "🥵", "🤔", "😎", "😲", "😭", "😞", "😴", "🤒", "🤢", "🥶"]
    lista = []
    num_pares = (filas * columnas) // 2

    for i in range(num_pares):
        lista.extend([lista_emotes[i], lista_emotes[i]])

    random.shuffle(lista)

    tablero = [lista[i * columnas:(i + 1) * columnas] for i in range(filas)]
    tablero_oculto = [["-" for _ in range(columnas)] for _ in range(filas)]

    return tablero, tablero_oculto

#metodo para mostrar el tablero
def mostrartablero(tablero):
    for fila in tablero:
        for celda in fila:
            print(" ", celda, end=" ")
        print()
        
#metodo para imprimir tablero, este es el que se usa
def imprimir_tablero(tablero):
    for fila in tablero:
        for celda in fila:
            if isinstance(celda, int) and celda < 10:
                print("  " + str(celda), end=" ")
            else:
                print(" " + str(celda), end=" ")
        print()

#metodo de juego que se trata de enfrentar una un jugador contra otro
def jugadorvsjugador(tablero, tablero_oculto, filas, columnas):
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

        distinta = False
        while not distinta:
            fila_revelar1 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): ")) - 1
            columna_revelar1 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): ")) - 1

            if tablero_oculto[fila_revelar1][columna_revelar1] != "-":
                print("Esa posición ya ha sido descubierta. Elige otra.")
                continue

            item1 = tablero[fila_revelar1][columna_revelar1]
            tablero_oculto[fila_revelar1][columna_revelar1] = item1

            print("\nTablero después de revelar la primera posición:")
            imprimir_tablero(tablero_oculto)

            while True:
                fila_revelar2 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): ")) - 1
                columna_revelar2 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): ")) - 1

                if (fila_revelar1 == fila_revelar2 and columna_revelar1 == columna_revelar2) or tablero_oculto[fila_revelar2][columna_revelar2] != "-":
                    print("Esa posición es la misma o ya ha sido descubierta. Elige otra.")
                else:
                    distinta = True
                    break

        item2 = tablero[fila_revelar2][columna_revelar2]
        tablero_oculto[fila_revelar2][columna_revelar2] = item2

        print("\nTablero después de revelar ambas posiciones:")
        imprimir_tablero(tablero_oculto)

        if item1 == item2:
            print("Felicidades, pareja encontrada")
            if jugador_actual:
                player1_puntuacion += 2
            else:
                player2_puntuacion += 2
        else:
            print("Has fallado, se cambia de turno.")
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = "-", "-"
            jugador_actual = not jugador_actual
                
        print(Jugador1, ": ", player1_puntuacion, "        ", Jugador2, ": ", player2_puntuacion)
        input("\nPulsa Enter para continuar...")
        if player1_puntuacion + player2_puntuacion >= (filas * columnas):
            print("Juego Terminado")

            if player1_puntuacion > player2_puntuacion:
                print("Felicidades ", Jugador1," has ganado con ", player1_puntuacion, "puntos")
            elif player1_puntuacion < player2_puntuacion:
                print("Felicidades ", Jugador2," has ganado con ", player2_puntuacion, "puntos")
            else:
                print("Los 2 jugadores han empatado con ", player1_puntuacion, " puntos")

            SN = input("¿Volver a jugar? S/N: ").upper()
            if SN == "S":
                opcionjuego()
            else:
                print("Saliendo del juego...")
                break
        

#medo de juego para que un jugador juegue contra una maquina
def jugadorvscpu(tablero, tablero_oculto, filas, columnas):

    # Memoria = {}

    Jugador = input("Introduce el nombre del Jugador: ")
    player_puntuacion = 0
    cpu_puntuacion = 0
    jugador_actual = True
    partida = True

    while partida:
        if jugador_actual:
            print("Turno de", Jugador)
            print("\nTablero actual:")
            imprimir_tablero(tablero_oculto)
            distinta = False

            # Selección de la primera posición
            while not distinta:
                fila_revelar1 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): ")) - 1
                columna_revelar1 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): ")) - 1

                if tablero_oculto[fila_revelar1][columna_revelar1] != "-":
                    print("Esa posición ya ha sido descubierta. Elige otra.")
                    continue

                item1 = tablero[fila_revelar1][columna_revelar1]
                tablero_oculto[fila_revelar1][columna_revelar1] = item1
                print("\nTablero después de revelar la primera posición:")
                imprimir_tablero(tablero_oculto)

                while True:
                    fila_revelar2 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): ")) - 1
                    columna_revelar2 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): ")) - 1

                    if (fila_revelar1 == fila_revelar2 and columna_revelar1 == columna_revelar2) or tablero_oculto[fila_revelar2][columna_revelar2] != "-":
                        print("Esa posición es la misma o ya ha sido descubierta. Elige otra.")
                    else:
                        distinta = True
                        break

                item2 = tablero[fila_revelar2][columna_revelar2]
                tablero_oculto[fila_revelar2][columna_revelar2] = item2
                print("\nTablero después de revelar ambas posiciones:")
                imprimir_tablero(tablero_oculto)

        

        else: 
            print("Turno de la máquina")
            distinta = False

            while not distinta:
                fila_revelar1, columna_revelar1 = random.randint(0, filas - 1), random.randint(0, columnas - 1)
                item1 = tablero[fila_revelar1][columna_revelar1]

                if tablero_oculto[fila_revelar1][columna_revelar1] == "-":
                    while True:
                        fila_revelar2, columna_revelar2 = random.randint(0, filas - 1), random.randint(0, columnas - 1)
                        if (fila_revelar1 != fila_revelar2 or columna_revelar1 != columna_revelar2) and tablero_oculto[fila_revelar2][columna_revelar2] == "-":
                            distinta = True
                            break

            item2 = tablero[fila_revelar2][columna_revelar2]
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = item1, item2
            print("\nTablero después de revelar ambas posiciones (CPU):")
            imprimir_tablero(tablero_oculto)
            print("La CPU mostró las cartas en las posiciones (" + str(fila_revelar1 + 1) + ", " + str(columna_revelar1 + 1) + ") y (" + str(fila_revelar2 + 1) + ", " + str(columna_revelar2 + 1) + ")")


        if item1 == item2:
            print("¡Pareja encontrada!")
            if jugador_actual:
                player_puntuacion += 2
            else:
                cpu_puntuacion += 2
        else:
            print("Has fallado, se cambia de turno.")
            tablero_oculto[fila_revelar1][columna_revelar1] = "-"
            tablero_oculto[fila_revelar2][columna_revelar2] = "-"
            jugador_actual = not jugador_actual
        
        print(Jugador + ": " + str(player_puntuacion) + "        CPU : " + str(cpu_puntuacion))
        

        input("\nPulsa Enter para continuar...")

        if player_puntuacion + cpu_puntuacion >= (filas * columnas):
            print("Juego Terminado")
            if player_puntuacion > cpu_puntuacion:
                print("¡Felicidades " + Jugador + ", has ganado con " + str(player_puntuacion) + " puntos!")
            elif player_puntuacion < cpu_puntuacion:
                print("La CPU ha ganado con ", cpu_puntuacion, " puntos")
            else:
                print("Has empatado con la CPU con ", player_puntuacion ," puntos")
                
            SN = input("¿Volver a jugar? S/N: ")
            if SN.upper() == "S":
                opcionjuego()
            else:
                print("Saliendo del juego...")
            break

        
#modo de juego para que juegue una maquina contra otra
def cpuvscpu(tablero, tablero_oculto, filas, columnas):
        
    cpu1_puntuacion = 0
    cpu2_puntuacion = 0
    jugador_actual = True
    partida = True
    while partida:
        if jugador_actual:
            print("Turno de la máquina 1")
            distinta = False

            while not distinta:
                fila_revelar1, columna_revelar1 = random.randint(0, filas - 1), random.randint(0, columnas - 1)
                if tablero_oculto[fila_revelar1][columna_revelar1] == "-":
                    while True:
                        fila_revelar2, columna_revelar2 = random.randint(0, filas - 1), random.randint(0, columnas - 1)
                        if (fila_revelar1 != fila_revelar2 or columna_revelar1 != columna_revelar2) and tablero_oculto[fila_revelar2][columna_revelar2] == "-":
                            distinta = True
                            break

            item1, item2 = tablero[fila_revelar1][columna_revelar1], tablero[fila_revelar2][columna_revelar2]
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = item1, item2
            print("\nTablero después de revelar ambas posiciones (CPU 1):")
            imprimir_tablero(tablero_oculto)
            print("La CPU 1 mostró las cartas en las posiciones (" + str(fila_revelar1 + 1) + ", " + str(columna_revelar1 + 1) + ") y (" + str(fila_revelar2 + 1) + ", " + str(columna_revelar2 + 1) + ")")
        else:
            print("Turno de la máquina 2")
            distinta = False

            while not distinta:
                fila_revelar1, columna_revelar1 = random.randint(0, filas - 1), random.randint(0, columnas - 1)
                if tablero_oculto[fila_revelar1][columna_revelar1] == "-":
                    while True:
                        fila_revelar2, columna_revelar2 = random.randint(0, filas - 1), random.randint(0, columnas - 1)
                        if (fila_revelar1 != fila_revelar2 or columna_revelar1 != columna_revelar2) and tablero_oculto[fila_revelar2][columna_revelar2] == "-":
                            distinta = True
                            break

            item1, item2 = tablero[fila_revelar1][columna_revelar1], tablero[fila_revelar2][columna_revelar2]
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = item1, item2
            print("\nTablero después de revelar ambas posiciones (CPU 2):")
            imprimir_tablero(tablero_oculto)
            print("La CPU 2 mostró las cartas en las posiciones (" + str(fila_revelar1 + 1) + ", " + str(columna_revelar1 + 1) + ") y (" + str(fila_revelar2 + 1) + ", " + str(columna_revelar2 + 1) + ")")

        
        if item1 == item2:
            print("¡Pareja encontrada!")
            if jugador_actual:
                cpu1_puntuacion += 2
            else:
                cpu2_puntuacion += 2
        else:
            print("Has fallado, se cambia de turno.")
            tablero_oculto[fila_revelar1][columna_revelar1] = "-"
            tablero_oculto[fila_revelar2][columna_revelar2] = "-"
            jugador_actual = not jugador_actual
        
        print("CPU 1 : " + str(cpu1_puntuacion) + "        CPU 2 : " + str(cpu2_puntuacion))
        input("\nPulsa Enter para continuar...")
            

        

        if cpu1_puntuacion + cpu2_puntuacion >= (filas * columnas):
            print("Juego Terminado")
            if cpu1_puntuacion > cpu2_puntuacion:
                print("Ha ganado la CPU 1 con ", cpu1_puntuacion , " puntos")
            else:
                print("Ha ganado la CPU 2 con ", cpu2_puntuacion , " puntos")
                
            SN = input("¿Volver a jugar? S/N: ")
            if SN.upper() == "S":
                opcionjuego()
            else:
                print("Saliendo del juego...")
                break
                


#metodo que muestra las reglas del juego
def reglas(): 
    print("\n\n")
    print("Las partidas son por turnos \nSi el jugador acierta una pareja en su truno, continua \nsi falla perdera el turno \n\nEl jugador que mas puntos tenga cuando se \ndescubra todo el tablero, ganara")

    SN =  input("¿Quieres jugar? S/N: ").upper()
    if(SN == "S"):
        opcionjuego()

#metodo que muestra un menu y elige el modo de juego seleccionado

def opcionjuego():
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

    print(f"\n{Fore.CYAN}{'=' * 40}")
    opcion = int(input("que opcion eliges: "))
    if opcion == 4:
        print("Saliendo....")
    else:
        filas, columnas = pedir_dimensiones()
        tablero, tablero_oculto = crear_tablero(filas, columnas)

    while True:
        match opcion:
            case 0:
                reglas()
            case 1:
                jugadorvsjugador(tablero, tablero_oculto, filas, columnas)
            case 2:
                jugadorvscpu(tablero, tablero_oculto, filas, columnas)
            case 3:
                cpuvscpu(tablero, tablero_oculto, filas, columnas)
            case _:
                print("Opción no válida")


opcionjuego()
