ra = int(input("Ingrese un numero: "))
rb = int(input("Ingrese otro numero: "))

while ra%rb != 0:
    ra, rb = rb, ra % rb

print(f"El MCD es: {rb}.")
