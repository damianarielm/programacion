texto = input("Ingrese un texto: ")

vocales = 0
for letra in texto:
    if letra in "aeiou":
        vocales += 1

print(f"La cantidad de vocales es: {vocales}.")
