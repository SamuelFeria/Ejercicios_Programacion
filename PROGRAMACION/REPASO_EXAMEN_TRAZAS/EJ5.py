suma = 0
positivos = 0
num = int(input("Número: "))
while num != 0:
    if num > 0:
        suma = suma + num
        positivos = positivos + 1
    num = int(input("Número: "))
print("Positivos:", positivos, "Suma:", suma)
