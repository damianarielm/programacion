montones =  ["*" * int(input("Ingrese cantidad del primer monton: "))]
montones += ["*" * int(input("Ingrese cantidad del segundo monton: "))]
montones += ["*" * int(input("Ingrese cantidad del tercer monton: "))]

turno = 0

while montones[0] or montones[1] or montones[2]:
    for i in range(len(montones)):
        print(f"{i + 1}: {montones[i]}")

    monton = int(input(f"Jugador {turno + 1}, elija un monton: ")) - 1

    if 0 <= monton <= 2 and montones[monton]:
        cantidad = int(input("Ingrese cantidad: "))

        if 0 < cantidad <= len(montones[monton]):
            montones[monton] = "*" * (len(montones[monton]) - cantidad)
            turno = (turno + 1) % 2
