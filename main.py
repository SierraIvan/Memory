import random
from colorama import Fore, Style, init



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

def mostrartablero():
    for fila in tablero:
        for celda in fila:
            print(" ", celda, end=" ")
        print()

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

        distinta = False
        while distinta == False:
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

            if fila_revelar1 == fila_revelar2 and columna_revelar1 == columna_revelar2:
                print("elige una posicion distinta")
                tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = "-", "-"
            else:
                distinta = True
        
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

       

        if player1_puntuacion + player2_puntuacion >= (filas * columnas) :

            print("Juego Terminado")

            if player1_puntuacion > player2_puntuacion:
                print("Felicidades ", Jugador1," has ganado con ", player1_puntuacion, "puntos")
            else:
                print("Felicidades ", Jugador2," has ganado con ", player2_puntuacion, "puntos")

            SN = input("¿Volver a jugar? S/N: ").upper
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
        
        if jugador_actual:
            print("\nTablero actual:")
            imprimir_tablero(tablero_oculto)
            distinta = False
            while not distinta:
                fila_revelar1 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): "))
                columna_revelar1 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): "))
                
                fila_revelar1 -= 1
                columna_revelar1 -= 1

                item1 = tablero[fila_revelar1][columna_revelar1]
                tablero_oculto[fila_revelar1][columna_revelar1] = item1

                print("\nTablero después de revelar la primera posición:")
                imprimir_tablero(tablero_oculto)

                # Pedimos la segunda posición
                fila_revelar2 = int(input("\nIntroduce la fila para revelar (1 - " + str(filas) + "): "))
                columna_revelar2 = int(input("Introduce la columna para revelar (1 - " + str(columnas) + "): "))
                
                fila_revelar2 -= 1
                columna_revelar2 -= 1

                if fila_revelar1 == fila_revelar2 and columna_revelar1 == columna_revelar2:
                    print("Elige una posición distinta")
                else:
                    distinta = True

            item2 = tablero[fila_revelar2][columna_revelar2]
            tablero_oculto[fila_revelar2][columna_revelar2] = item2

            print("\nTablero después de revelar ambas posiciones:")
            imprimir_tablero(tablero_oculto)

        else:  
            distinta = False
            while not distinta:
                fila_revelar1, columna_revelar1 = random.randint(0, filas - 1), random.randint(0, columnas - 1)

                fila_revelar2,  columna_revelar2 = random.randint(0, filas - 1),  random.randint(0, columnas - 1)
                

                if fila_revelar1 != fila_revelar2 or columna_revelar1 != columna_revelar2:
                    distinta = True
            item1, item2 = tablero[fila_revelar1][columna_revelar1], tablero[fila_revelar2][columna_revelar2]
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = item1 , item2
            

            print("\nTablero después de revelar ambas posiciones (CPU):")
            imprimir_tablero(tablero_oculto)
            print("La CPU mostró las cartas en las posiciones (" + str(fila_revelar1 + 1) + ", " + str(columna_revelar1 + 1) + ") y (" + str(fila_revelar2 + 1) + ", " + str(columna_revelar2 + 1) + ")")


        if item1 == item2:
            print("¡Pareja encontrada!")
            if jugador_actual:
                player_puntuacion += 1
            else:
                cpu_puntuacion += 1
        else:
            print("Has fallado, se cambia de turno.")
            tablero_oculto[fila_revelar1][columna_revelar1], tablero_oculto[fila_revelar2][columna_revelar2] = "-" , "-"
            jugador_actual = not jugador_actual
                
        print(Jugador, ": ", player_puntuacion, "        CPU : ", cpu_puntuacion)
        input("\nPulsa Enter para continuar...")


        if player_puntuacion + cpu_puntuacion >= (filas * columnas) // 2:
            print("Juego Terminado")

            if player_puntuacion > cpu_puntuacion:
                print("¡Felicidades" ,Jugador, ", has ganado con" , player_puntuacion, "puntos!")
            else:
                print("La CPU ha ganado")
                
            SN = input("¿Volver a jugar? S/N: ")
            if SN.upper() == "S":
                opcionjuego()
            else:
                print("Saliendo del juego...")
                break
        
    



def cpuvscpu():
    print("hola")

def reglas(): 
    print("\n\n")
    print("Las partidas son por turnos \nSi el jugador acierta una pareja en su truno, continua \nsi falla perdera el turno \n\nEl jugador que mas puntos tenga cuando se \ndescubra todo el tablero, ganara")

    SN =  input("¿Quieres jugar? S/N: ").upper()
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

filas = int(input("Dime cuántas filas quieres que tenga el tablero: "))
columnas = int(input("Dime cuántas columnas quieres que tenga el tablero: "))


while (filas * columnas) % 2 != 0 or filas > 5 or columnas > 6:
    if filas > 5 or columnas > 6:
        print("Lo máximo permitido para el tablero es 5 x 6")
    else:
        print("La multiplicación de filas x columnas tiene que dar par")
    
    filas = int(input("Dime cuántas filas quieres que tenga el tablero: "))
    columnas = int(input("Dime cuántas columnas quieres que tenga el tablero: "))


tablero, tablero_oculto = crear_tablero(filas, columnas)

opcionjuego()
