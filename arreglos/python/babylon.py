pilas = ["♥"] * 3 + ["♦"] * 3 + ["♣"] * 3 + ["♠"] * 3

turno = 0
fin = False
while not fin:
    for i, pila in enumerate(pilas): print(f"{i}: {pila}")

    print(f"Turno jugador {turno + 1}.")
    origen = pilas[int(input("Ingrese pila de origen: "))]
    destino = pilas[int(input("Ingrese pila de destino: "))]

    if origen[-1] == destino[-1] or len(origen) == len(destino):
        pilas += [destino + origen]
        pilas.remove(origen)
        pilas.remove(destino)
    else:
        print("Movimiento invalido.")
        fin = True

    turno = (turno + 1) % 2

print(f"Gana el jugador {turno + 1}.")
