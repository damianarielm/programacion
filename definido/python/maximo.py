maximo = int(input("Ingrese un numero: "))

for _ in range(10):
    numero = int(input("Ingrese otro numero: "))

    if numero > maximo: maximo = numero

print(f"El numero mayor es: {maximo}.")
