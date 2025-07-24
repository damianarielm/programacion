positivos = negativos = 0
numero = 1

while numero != 0:
    numero = int(input("Ingrese un numero (0 para salir): "))
    if numero > 0:
        positivos =+ 1
    elif numero < 0:
        negativos =+ 1

print("La cantidad de numeros positivos es:", positivos)
print("La cantidad de numeros negativos es:", negativos)
