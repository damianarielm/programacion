numero = int(input("Ingrese un numero: "))

print("Los divisores son:")
for divisor in (1, numero + 1):
    if numero % divisor == 0:
        print(divisor)
