#El usuario introduce: 44, 0, 38. Cuidado con el 0.
for vuelta in range(3):
    n = int(input("Número: "))
    suma = 0
    while n > 0:
        suma = suma + n % 10
        n = n // 10
    match suma:
        case 0:
            print("Cero")
        case s if s % 2 == 0:
            print(s, "par")
        case _:
            print("impar")