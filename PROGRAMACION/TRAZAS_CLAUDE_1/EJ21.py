#El usuario introduce: 9, 4, -2, 7, 0.

mayores = 0
suma = 0
num = int(input("Número: "))
while num != 0:
    if num > 5:
        mayores = mayores + 1
    elif num < 0:
        suma = suma + num
    num = int(input("Número: "))
print("Mayores:", mayores, "Suma:", suma)