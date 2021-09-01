for retrato in range(1, 3 + 1):
    cofre1 = retrato == 1
    cofre2 = retrato != 2
    cofre3 = retrato != 1

    solo1 = cofre1 and not cofre2 and not cofre3
    solo2 = not cofre1 and cofre2 and not cofre3
    solo3 = not cofre1 and not cofre2 and cofre3
    ninguna = not cofre1 and not cofre2 and not cofre3

    if solo1 or solo2 or solo3 or ninguna:
        print(f"El retrato esta en el cofre {retrato}.")
