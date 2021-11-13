año = int(input("Ingrese el año: "))

if año%4 == 0 and (año%100 != 0 or año%400 == 0):
    print("El año es bisiesto.")
else
    print("El año es no bisiesto.")
