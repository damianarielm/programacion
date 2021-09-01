n = int(input("Ingrese un numero menor a 4000: "))
romanos = ""

romanos, n = romanos + "M" * (n // 1000), n % 1000
romanos, n = romanos + "CM" * (n // 900), n % 900
romanos, n = romanos + "D" * (n // 500), n % 500
romanos, n = romanos + "CD" * (n // 400), n % 400
romanos, n = romanos + "C" * (n // 100), n % 100
romanos, n = romanos + "XC" * (n // 90), n % 90
romanos, n = romanos + "L" * (n // 50), n % 50
romanos, n = romanos + "XL" * (n // 40), n % 40
romanos, n = romanos + "X" * (n // 10), n % 10
romanos, n = romanos + "IX" * (n // 9), n % 9
romanos, n = romanos + "V" * (n // 5), n % 5
romanos, n = romanos + "IV" * (n // 4), n % 4
romanos, n = romanos + "I" * (n // 1), n % 1

print(f"El numero en decimal es: {romanos}.")
