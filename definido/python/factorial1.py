n = int(input("Ingrese un numero: "))

factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(f"El factorial es: {factorial}.")
