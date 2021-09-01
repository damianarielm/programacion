n = int(input("Ingrese un numero: "))

for factor in range(1, n + 1):
    if n % factor == 0:
        print(factor)
