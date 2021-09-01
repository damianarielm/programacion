n = int(input("Ingrese un numero mayor a 1: "))
factor = 2
primo = True

while n >= 4 and factor <= int(n ** 0.5) + 1 and primo:
    if n % factor == 0: primo = False
    else: factor += 1

print(f"El numero{' no' if not primo else ''} es primo.")
