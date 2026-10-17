contador = 0
for x in range(10, 4, -2):
    if x % 4 == 0:
        contador = contador + 1
        print(x, "es múltiplo de 4")
    else:
        print(x, "no lo es")
print("Múltiplos de 4:", contador)
