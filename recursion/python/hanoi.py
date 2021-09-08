def mover(altura, origen, destino, auxiliar):
    if altura >= 1:
        mover(altura - 1, origen, auxiliar, destino)
        print(origen, "->", destino)
        mover(altura - 1, auxiliar, destino, origen)

discos = int(input("Ingrese numero de discos: "))
mover(discos, 1, 3, 2)
