def medio(palabra):
    if len(palabra) <= 1:
        return palabra

    return medio(palabra[1:-1])

palabra = input("Ingrese una palabra: ")

print(f"La letra del medio es: '{medio(palabra)}'.")
