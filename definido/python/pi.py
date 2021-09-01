iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

pi = 0
for i in range(iteraciones):
    pi += (-1)**i / (2*i + 1)
pi *= 4

print(f"El valor calculado de pi es: {pi}.")
