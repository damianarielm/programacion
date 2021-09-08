iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

pi = 1
for i in range(1, iteraciones + 1):
    pi *= (2*i / (2*i - 1)) * (2*i / (2*i + 1))
pi *= 2

print(f"El valor calculado de pi es: {pi}.")
