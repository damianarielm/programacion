n = int(input("Ingrese un numero: "))

for i in range(n - 1, 0, -1):
    n *= i

print(f"El factorial es: {n}.")
