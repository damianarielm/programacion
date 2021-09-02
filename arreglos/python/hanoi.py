discos = int(input("Ingrese numero de discos: "))

torres = [ list(range(discos))[::-1], [], [] ]

while len(torres[2]) != discos:
    for i in range(len(torres)):
        print(f"Torre {i + 1}: {torres[i]}.")

    origen = int(input("Ingrese torre de origen: ")) - 1
    destino = int(input("Ingrese torre de destino: ")) - 1

    if origen < 4 and destino < 4 and torres[origen]:
        if not torres[destino] or torres[origen][-1] < torres[destino][-1]:
            torres[destino] += [ torres[origen].pop() ]

print("Ganaste!")
