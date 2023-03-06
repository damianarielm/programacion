def merge(lista1, lista2):
    if not lista1:
        return lista2
    elif not lista2:
        return lista1
    elif lista1[0] < lista2[0]:
        return [ lista1[0] ] + merge(lista1[1:], lista2)
    else:
        return [ lista2[0] ] + merge(lista1, lista2[1:])
