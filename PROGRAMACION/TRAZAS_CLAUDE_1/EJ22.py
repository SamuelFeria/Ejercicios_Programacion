#El usuario introduce: 1, 1, 1, 2, 1, 3. Ojo: aquí ningún case pide una segunda cantidad, y hay dos case 1.

libres = 2
opcion = 0
while opcion != 3:
    opcion = int(input("Opción: "))
    match opcion:
        case 1 if libres > 0:
            libres = libres - 1
            print("Entra")
        case 1:
            print("Completo")
        case 2:
            libres = libres + 1
            print("Sale")
        case 3:
            print("Fin", libres)