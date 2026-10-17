for vuelta in range(2):
    n = int(input("Número: "))
    cifras = 0
    while n > 0:
        n = n // 10
        cifras = cifras + 1
    match cifras:
        case 1:
            print("Una cifra")
        case c if c <= 3:
            print(c, "cifras")
        case _:
            print("Muchas cifras")
