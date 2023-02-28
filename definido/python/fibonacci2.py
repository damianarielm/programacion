cantidad = int(input("Ingrese la cantidad de numeros: "))

phi = (1 + 5**0.5) / 2

for n in range(1, cantidad + 1):
    print( (phi**n - (1 - phi)**n) // (5**0.5) )
