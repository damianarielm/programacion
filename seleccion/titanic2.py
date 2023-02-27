sexo = input("Ingrese sexo (F/M): ")
edad = int(input("Ingrese la edad: "))
hermanos = int(input("Ingrese cantidad de hermanos: "))

if sexo == "F" or edad > 9.5 and hermanos > 2.5:
    print("La persona sobrevivio.")
else:
    print("La persona no sobrevivio.")
