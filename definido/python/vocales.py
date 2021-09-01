texto = input("Ingrese un texto: ")

vocales = 0
for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales += 1

print(f"La cantidad de vocales es: {vocales}.")
