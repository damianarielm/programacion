año = int(input("Ingrese el año: "))

if año%4 == 0:
    if año%100 == 0:
        if año%400 == 0:
            print("El año es bisiesto.")
        else
            print("El año no es bisiesto.")
    else:
        print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
