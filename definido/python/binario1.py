n = input("Ingrese un numero en binario: ")
decimal = 0

for i, digito in enumerate(n):
    if digito == "1":
        decimal += 2 ** (len(n) - 1 - i)

print(f"El numero en decimal es: {decimal}.")
