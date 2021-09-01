n = int(input("Ingrese un numero positivo: "))
binario = ""

while n >= 1:
    binario = str(n % 2) + binario
    n //= 2

print(f"El numero en binario es: {binario}.")
