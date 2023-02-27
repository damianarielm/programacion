sexo = input("Ingrese sexo (F/M): ")
edad = int(input("Ingrese la edad: "))
hermanos = int(input("Ingrese cantidad de hermanos: "))

if sexo == "M":
    if edad > 9.5:
        if hermanos > 2.5:
            print("El pasajero sobrevivio.")
        else:
            print("El pasajero no sobrevivio.")
    else:
        print("El pasajero no sobrevivio.")
else:
    print("La pasajera sobrevivio.")
