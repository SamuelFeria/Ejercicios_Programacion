n = 253
suma = 0
while n > 0:
    suma = suma + n % 10
    n = n // 10
print("Suma:", suma)