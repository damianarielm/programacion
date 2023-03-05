lista = [200, 190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

def ordenar(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [ n for n in lista[1:] if n < pivote ]
        mayores = [ n for n in lista[1:] if n >= pivote ]
        return ordenar(menores) + [ pivote ] + ordenar(mayores)

print(f"Lista ordenada: {ordenar(lista)}.")
