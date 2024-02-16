n = int(input("Ingrese un numero: "))

suma = 0
while n != 0:
    suma += n % 10
    n //= 10

print(f"La suma de los digitos es: {suma}.")
