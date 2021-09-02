def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Ingrese un numero: "))

print(f"El factorial es: {factorial(n)}.")
