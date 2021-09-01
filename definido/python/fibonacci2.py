phi = (1 + 5**0.5) / 2

for n in range(1, 10):
    print( (phi**n - (1 - phi)**n) // (5**0.5) )
