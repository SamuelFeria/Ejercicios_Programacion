#El usuario introduce, en este orden: 7, 0, 58, 66. Piensa la solución sin ejecutar el código.

for vuelta in range(4):
    n = int(input("Número: "))
    suma = 0
    while n > 0:
        suma = suma + n % 10
        n = n // 10
    match suma:
        case 0:
            print("Cero")
        case s if s < 10:
            print(s, "una cifra")
        case s if s % 2 == 0:
            print(s, "par")
        case _:
            print("impar")