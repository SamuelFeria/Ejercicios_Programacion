#El usuario introduce, en este orden: 2, 30, 1, 15, 4, 2, 30, 3.

puntos = 20
opcion = 0
while opcion != 3:
    opcion = int(input("Opción: "))
    match opcion:
        case 1:
            cantidad = int(input("Sumar: "))
            puntos = puntos + cantidad
        case 2:
            cantidad = int(input("Restar: "))
            if cantidad <= puntos:
                puntos = puntos - cantidad
            else:
                print("Insuficiente")
        case 3:
            print("Total:", puntos)
        case _:
            print("Error")