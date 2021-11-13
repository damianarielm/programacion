maximo = int(input("Ingrese un numero: "))

for _ in range(10):
    maximo = max(maximo, int(input("Ingrese otro numero: ")))

print(f"El numero mayor es: {maximo}.")
