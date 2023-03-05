def insertar_en_orden(lista, numero):
    mitad = len(lista) // 2

    if len(lista) == 0:
        return [numero]
    if len(lista) == 1:
        return [numero] + lista if numero < lista[0] else lista + [numero]
    elif numero <= lista[mitad]:
        return insertar_en_orden(lista[:mitad], numero) + lista[mitad:]
    else:
        return lista[:mitad] + insertar_en_orden(lista[mitad:], numero)

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    lista = list(range(cantidad))

    numero = float(input("Ingrese numero a agregar: "))
    lista = insertar_en_orden(lista, numero)

    print(f"Lista: {lista}.")
