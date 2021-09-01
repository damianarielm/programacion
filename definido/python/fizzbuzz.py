maximo = int(input("Ingrese el maximo: "))

for numero in range(maximo + 1):
    if numero % 15 == 0: print("fizzbuzz")
    elif numero % 3 == 0: print("fizz")
    elif numero % 5 == 0: print("buzz")
    else: print(numero)
