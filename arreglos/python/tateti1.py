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

    if 0 < tablero[0][0] == tablero[0][1] == tablero[0][2]: fin = True
    if 0 < tablero[1][0] == tablero[1][1] == tablero[2][2]: fin = True
    if 0 < tablero[2][0] == tablero[2][1] == tablero[2][2]: fin = True
    if 0 < tablero[0][0] == tablero[1][0] == tablero[2][0]: fin = True
    if 0 < tablero[0][1] == tablero[1][1] == tablero[2][1]: fin = True
    if 0 < tablero[0][2] == tablero[1][2] == tablero[2][2]: fin = True
    if 0 < tablero[0][0] == tablero[1][1] == tablero[2][2]: fin = True
    if 0 < tablero[0][2] == tablero[1][1] == tablero[2][0]: fin = True
    if 0 not in tablero[0] + tablero[1] + tablero[2]: fin = True
