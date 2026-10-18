cont = 0
suma = 0
for n in range(1, 16):
    if 15 % n == 0:
        cont = cont + 1
        suma = suma + n
        print(n)
print(cont, suma)