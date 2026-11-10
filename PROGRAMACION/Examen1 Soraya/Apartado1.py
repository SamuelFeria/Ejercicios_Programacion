print("==================")
print("ELIGE UN LUCHADOR")
print("==================")
print("Elige [1] para añadir estadisticas a tu luchador")
menu = input("Elige una opción o escribe 'salir' para salir del programa: ")
luchador1=""
luchador2=""
while menu != "salir":
    match menu:
        case "1":
                luchadores = input("Introdoce luchador1 o luchador2: ")
                if luchadores == "luchador1":
                    nombre = input("Introduce nombre del luchador: ")
                    tipo = input("Elige entre 'T' (Tanque) o 'N'(Normal): ").upper()
                    if tipo == "T":
                        print("Elegiste tanque")
                        vida = int(input("Introduce la vida del tanque: "))
                        daño = int(input("Introduce el daño del tanque: "))
                        print(nombre,"(Tanque)","-",vida,"-",daño)
                    else: 
                        print("Elegiste normal")
                        vida = int(input("Introduce la vida del tanque: "))
                        daño = int(input("Introduce el daño del tanque: "))
                        print(nombre,"(Normal)","-",vida,"-",daño)
                elif luchadores == "luchador1":
                    nombre = input("Introduce nombre del luchador")
                    tipo = input("Elige entre 'T' (Tanque) o 'N'(Normal): ").upper()
                    if tipo == "T":
                        print("Elegiste tanque")
                        vida = int(input("Introduce la vida del tanque: "))
                        daño = int(input("Introduce el daño del tanque: "))
                        print(nombre,"(Tanque)","-",vida,"-",daño)
                    else: 
                        print("Elegiste normal")
                        vida = int(input("Introduce la vida del tanque: "))
                        daño = int(input("Introduce el daño del tanque: "))
                        print(nombre,"(Normal)","-",vida,"-",daño) 
               
        case _: 
            print()
    print("==================")
    print("ELIGE UN LUCHADOR")
    print("==================")
    print("Elige [1] para añadir estadisticas a tu luchador")
    print("Escribe 'salir' para salir del programa")
    menu = input("Elige una opción o escribe 'salir' para salir del programa: ")
print("FIN")        
