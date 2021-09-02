alfabeto = "abcdefghijklmnopqrstuvwxyz"

texto = input("Ingrese un texto: ")
desplazamiento = int(input("Ingrese desplazamiento: "))
cifrado = ""

for letra in texto:
    indice = (alfabeto.index(letra) + desplazamiento) % len(alfabeto)
    cifrado += alfabeto[indice]

print(f"El texto cifrado es: {cifrado}.")
