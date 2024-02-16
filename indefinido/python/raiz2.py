n = int(input("Ingrese un numero: "))

raiz = (n - 1) % 9 + 1 if n else 0

print(f"La raiz digital es: {raiz}.")
