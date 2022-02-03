fila1 = [ 5, 3, 4, 6, 7, 8, 9, 1, 2 ]
fila2 = [ 6, 7, 2, 1, 9, 5, 3, 4, 8 ]
fila3 = [ 1, 9, 8, 3, 4, 2, 5, 6, 7 ]
fila4 = [ 8, 5, 9, 7, 6, 1, 4, 2, 3 ]
fila5 = [ 4, 2, 6, 8, 5, 3, 7, 9, 1 ]
fila6 = [ 7, 1, 3, 9, 2, 4, 8, 5, 6 ]
fila7 = [ 9, 6, 1, 5, 3, 7, 2, 8, 4 ]
fila8 = [ 2, 8, 7, 4, 1, 9, 6, 3, 5 ]
fila9 = [ 3, 4, 5, 2, 8, 6, 1, 7, 9 ]
tablero = [ fila1, fila2, fila3, fila4, fila5, fila6, fila7, fila8, fila9 ]

for i, fila in enumerate(tablero):
    if len(fila) != len(set(fila)) or 0 in fila:
        print(f"Error en la fila {i + 1}.")
        exit(1)

for i, columna in enumerate(zip(*tablero)):
    if len(columna) != len(set(columna)) or 0 in columna:
        print(f"Error en la columna {i + 1}.")
        exit(2)

for i, j in zip(range(0, 3, 3), range(0, 3, 3)):
    cuadrado = []
    for di, dj in zip(range(3), range(3)):
        cuadrado.append(tablero[i + di][j + dj])

    if len(cuadrado) != len(set(cuadrado)) or 0 in cuadrado:
        print(f"Error en el cuadrado {i + di + 1}, {j + dj + 1}")
        exit(3)

print("Valido.")
