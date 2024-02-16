n = raiz = int(input("Ingrese un numero: "))

while n > 9:
    raiz = 0
    while n != 0:
        raiz += n % 10
        n //= 10
    n = raiz

print(f"La raiz digital es: {raiz}.")
