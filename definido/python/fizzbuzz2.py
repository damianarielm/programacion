maximo = int(input("Ingrese el maximo: "))

for numero in range(1, maximo + 1):
    respuesta = ""
    if numero % 3 == 0: respuesta += "fizz"
    if numero % 5 == 0: respuesta += "buzz"
    print(numero if not respuesta else respuesta)
