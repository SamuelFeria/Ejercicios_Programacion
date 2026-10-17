#El usuario introduce, en este orden: 3, 8, -2, 5, 0. Haz la traza y anota qué se imprime
suma = 0
pares = 0
num = int(input("Número: "))
while num != 0:
    if num % 2 == 0:
        pares = pares + 1
        suma = suma + num
    else:
        suma = suma - 1
    num = int(input("Número: "))
print("Pares:", pares, "Suma:", suma)