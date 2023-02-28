n = input("Ingrese un numero en binario: ")
decimal = 0

for potencia, digito in enumerate(reversed(n)):
    if digito == "1":
        decimal += 2 ** potencia

print(f"El numero en decimal es: {decimal}.")
