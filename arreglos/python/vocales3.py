texto = input("Ingrese un texto: ")

vocales  = texto.count("a")
vocales += texto.count("e")
vocales += texto.count("i")
vocales += texto.count("o")
vocales += texto.count("u")

print(f"La cantidad de vocales es: {vocales}.")
