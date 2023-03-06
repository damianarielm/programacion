tablero = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
turno = 0
fin = False

for fila in tablero: print(fila)
while not fin:
    print(f"Turno: jugador {turno + 1}")
    fila = int(input("Ingrese fila: ")) - 1
    columna = int(input("Ingrese columna: ")) - 1

    if not tablero[fila][columna]:
        tablero[fila][columna] = turno + 1
        turno = (turno + 1) % 2

    for fila in tablero: print(fila)

    sumas  = [ sum(fila) for fila in tablero if 0 not in fila ]
    sumas += [ sum(columna) for columna in zip(*tablero) if 0 not in columna ]
    diagonal1 = 0 < tablero[0][0] == tablero[1][1] == tablero[2][2]
    diagonal2 = 0 < tablero[2][2] == tablero[1][1] == tablero[2][0]
    empate = 0 not in tablero[0] + tablero[1] + tablero[2]
    fin = 3 in sumas or 6 in sumas or diagonal1 or diagonal2 or empate
