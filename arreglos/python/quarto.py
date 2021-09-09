from colorama import Fore, Style

def mostrarTablero(tablero):
    print("\nTablero:")
    for fila in tablero:
        print(*[elemento[0] for elemento in fila])
    print("")

tablero = [ [" "] * 4 for _ in range(4) ]
piezas  = [ ("o" + Style.RESET_ALL, 0, 0, 0, 0) ]
piezas += [ (Style.BRIGHT + "o" + Style.RESET_ALL, 0, 0, 0, 1) ]
piezas += [ (Fore.YELLOW + "o" + Style.RESET_ALL, 0, 0, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "o" + Style.RESET_ALL, 0, 0, 1, 1) ]
piezas += [ ("O" + Style.RESET_ALL, 0, 1, 0, 0) ]
piezas += [ (Style.BRIGHT + "O" + Style.RESET_ALL, 0, 1, 0, 1) ]
piezas += [ (Fore.YELLOW + "O" + Style.RESET_ALL, 0, 1, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "O" + Style.RESET_ALL, 0, 1, 1, 1) ]
piezas += [ ("x" + Style.RESET_ALL, 1, 0, 0, 0) ]
piezas += [ (Style.BRIGHT + "x" + Style.RESET_ALL, 1, 0, 0, 1) ]
piezas += [ (Fore.YELLOW + "x" + Style.RESET_ALL, 1, 0, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "x" + Style.RESET_ALL, 1, 0, 1, 1) ]
piezas += [ ("X" + Style.RESET_ALL, 1, 1, 0, 0) ]
piezas += [ (Style.BRIGHT + "X" + Style.RESET_ALL, 1, 1, 0, 1) ]
piezas += [ (Fore.YELLOW + "X" + Style.RESET_ALL, 1, 1, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "X" + Style.RESET_ALL, 1, 1, 1, 1) ]

jugador = ganador = 0
while not ganador:
    mostrarTablero(tablero)
    for i, pieza in enumerate(piezas): print(f"{i}: {pieza[0]}")
    pieza = input(f"\nJugador {jugador+1} elija una pieza para su oponente: ")
    pieza = piezas.pop(int(pieza))

    jugador = (jugador + 1) % 2
    fila = int(input(f"\nJugador {jugador+1} ingrese fila: ")) - 1
    columna = int(input(f"Jugador {jugador+1} ingrese columna: ")) - 1
    tablero[fila][columna] = pieza

    d1 = [ tablero[0][0], tablero[1][1], tablero[2][2], tablero[3][3] ]
    d2 = [ tablero[0][3], tablero[1][2], tablero[2][1], tablero[3][0] ]
    for posibilidad in tablero + list(zip(*tablero)) + [d1, d2]:
        if " " not in posibilidad:
            for i in range(1, 5):
                if all(pieza[i] == posibilidad[0][i] for pieza in posibilidad):
                    ganador = jugador + 1

mostrarTablero(tablero)
print(f"Jugador {ganador} ha ganado!")
