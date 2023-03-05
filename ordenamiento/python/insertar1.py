def insertar_en_orden(lista, numero):
    for i in range(len(lista)): # Recorremos la lista...
        if numero < lista[i]: # ...buscando un lugar en el medio.
            return lista[:i] + [numero] + lista[i:]

    return lista + [elemento]   # Si no lo encontramos, va al final.

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    lista = list(range(cantidad))

    numero = float(input("Ingrese numero a agregar: "))
    lista = insertar_en_orden(lista, numero)

    print(f"Lista: {lista}.")
