opcion = ""
while opcion != "0":
    print("Menu principal")
    print("1 - Menu secundario")
    print("2 - Menu terciario")
    print("0 - Salir")
    opcion = input("Ingrese una opcion: ")
    print("")

    if opcion == "1":
        while opcion != "0":
            print("Menu secundario")
            print("1 - Opcion 1")
            print("2 - Opcion 2")
            print("0 - Volver")
            opcion = input("Ingrese una opcion: ")
            print("")
        opcion = ""
    elif opcion == "2":
        while opcion != "0":
            print("Menu terciario")
            print("1 - Opcion 1")
            print("2 - Opcion 2")
            print("0 - Volver")
            opcion = input("Ingrese una opcion: ")
            print("")
        opcion = ""
