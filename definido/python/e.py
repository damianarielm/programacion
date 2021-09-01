iteraciones = int(input("Ingrese cantidad de iteraciones: "))

e = 1
factorial = 1
for i in range(1, iteraciones):
    e += 1 / factorial
    factorial *= i + 1

print(f"El valor de e es: {e}.")
