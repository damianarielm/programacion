texto = input("Ingrese un texto: ")

print("La cadena reversa es:", end = " ")
for indice in range(len(texto)):
    print(f"{texto[len(texto) - 1 - indice]}", end = "")
