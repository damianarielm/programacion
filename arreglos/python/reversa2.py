texto = input("Ingrese un texto: ")

print("La cadena reversa es:", end = " ")
for indice in range(len(texto) - 1, -1, -1):
    print(f"{texto[indice]}", end = "")
