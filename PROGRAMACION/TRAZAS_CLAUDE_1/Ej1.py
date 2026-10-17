n = 7
pasos = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    pasos = pasos + 1
print("Pasos:", pasos)
