from random import shuffle

dorso = "██"
valores = "A234567890JQK"
palos = "♥♤♢♧"
rojos = "♥♢"
coincidencias = 0

mazo = [ valor + palo for valor in valores for palo in palos ]
shuffle(mazo)

matriz = []
for i in range(len(palos)):
    matriz += [ mazo[len(valores) * i:len(valores) * (i+1)] ]

juego = [ [dorso] * len(valores) for _ in palos ]

while coincidencias < len(mazo) / 2:
    print("   1   2   3   4   5   6   7   8   9   10  11  12  13")
    for i, fila in enumerate(juego):
        print(i + 1, *fila, sep = "  ", end = "\n\n")

    fila1 = int(input("Ingrese una fila: ")) - 1
    columna1 = int(input("Ingrese una columna: ")) - 1
    carta1 = matriz[fila1][columna1]
    print(f"\n{carta1}\n")

    fila2 = int(input("Ingrese una fila: ")) - 1
    columna2 = int(input("Ingrese una columna: ")) - 1
    carta2 = matriz[fila2][columna2]
    print(f"\n{carta2}\n")

    ambosRojos = carta1[1] in rojos and carta2[1] in rojos
    ambosNegros = carta1[1] not in rojos and carta2[1] not in rojos
    if carta1[0] == carta2[0] and (ambosRojos or ambosNegros):
        juego[fila1][columna1] = carta1
        juego[fila2][columna2] = carta2
        coincidencias += 1

print("Ganaste!")
