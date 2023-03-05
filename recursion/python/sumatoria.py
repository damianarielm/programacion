def sumatoria(numero):
    if numero <= 0:
        return numero
    else:
        return numero + sumatoria(numero - 1)

numero = int(input("Ingrese un numero: "))
print(f"La suma es: {sumatoria(numero)}.")
