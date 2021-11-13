texto = input("Ingrese texto: ")
codigo = ""

for letra in texto:
    if letra == "a": codigo += ".- "
    elif letra == "b": codigo += "-... "
    elif letra == "c": codigo += "-.-. "
    elif letra == "d": codigo += "-.. "
    elif letra == "e": codigo += ". "
    elif letra == "f": codigo += "..-. "
    elif letra == "g": codigo += "--. "
    elif letra == "h": codigo += ".... "
    elif letra == "i": codigo += ".. "
    elif letra == "j": codigo += ".--- "
    elif letra == "k": codigo += "-.- "
    elif letra == "l": codigo += ".-.. "
    elif letra == "m": codigo += "-- "
    elif letra == "n": codigo += "-. "
    elif letra == "o": codigo += "--- "
    elif letra == "p": codigo += ".--. "
    elif letra == "q": codigo += "--.- "
    elif letra == "r": codigo += ".-. "
    elif letra == "s": codigo += "... "
    elif letra == "t": codigo += "- "
    elif letra == "u": codigo += "..- "
    elif letra == "v": codigo += "...- "
    elif letra == "w": codigo += ".-- "
    elif letra == "x": codigo += "-..- "
    elif letra == "y": codigo += "-.-- "
    elif letra == "z": codigo += "--.. "
    else: codigo += letra

print(f"El cifrado es: {codigo}")
