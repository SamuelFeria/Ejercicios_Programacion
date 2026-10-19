#El usuario introduce, en este orden: 7, 0, 58, 125.
total = 0
for vuelta in range(4):
    n = int(input("Número: "))
    cifras = 0
    suma = 0
    while n > 0:
        suma = suma + n % 10
        n = n // 10
        cifras = cifras + 1
    match cifras:
        case 0:
            print("Vacío")
        case 1:
            total = total + suma
        case c if suma % 2 == 0:
            total = total + c
            print(suma, "par")
        case _:
            print(suma * 2)
print("Total:", total)