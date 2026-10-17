saldo = 100
opcion = 0
while opcion != 3:
    opcion = int(input("Opción: "))
    match opcion:
        case 1:
            cantidad = int(input("Ingresar: "))
            saldo = saldo + cantidad
        case 2:
            cantidad = int(input("Retirar: "))
            if cantidad <= saldo:
                saldo = saldo - cantidad
            else:
                print("Saldo insuficiente")
        case 3:
            print("Saldo final:", saldo)
