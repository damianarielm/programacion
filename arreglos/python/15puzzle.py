tablero = [ [1, 2, 0, 3], [9, 8, 4, 7], [6, 5, 11, 12], [13, 10, 14, 15] ]
final = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0] ]

while tablero != final:
    for fila in tablero:
        for elemento in fila:
            print(f"{elemento:02d}", end = " ")
        print("")

    print("\n8 - Arriba.")
    print("4 - Izquierda.")
    print("6 - Derecha.")
    print("2 - Abajo.")
    movimiento = int(input("Ingrese un movimiento: "))

    for i, fila in enumerate(tablero):
        for j, elemento in enumerate(fila):
            if elemento == 0:
                x, y = i, j

    if movimiento == 8:
        tablero[x][y], tablero[x - 1][y] = tablero[x - 1][y], tablero[x][y]
    elif movimiento == 2:
        tablero[x][y], tablero[x + 1][y] = tablero[x + 1][y], tablero[x][y]
    elif movimiento == 4:
        tablero[x][y], tablero[x][y - 1] = tablero[x][y - 1], tablero[x][y]
    else:
        tablero[x][y], tablero[x][y + 1] = tablero[x][y + 1], tablero[x][y]

print("Ganaste!")
