#pide al usuario que elige un menú
menu = int(input("Elige ente el menu 1 o otros: "))
#si elige el 1
match menu:
    case 1:
        print("Has seleccionado el apartado 1.")
        #pide una cadena por teclado y escribe por pantalla cada caracter de una cadena introducida por teclado
        cadena = input("Introduce una cadena: ")
        for i in range (len(cadena)):
            caracterCadena = cadena[i]
            print(caracterCadena)
    #si elige otro
    case _:
        print("Has seleccionado otro apartado.")
        #te pide un caracter por teclado y el sistema contara el % de veces que aparece ese caracter que se ha introducido por teclado
        cadena = input("introduce una cadena: ")
        caracter = input("introduce un caracter: ")
        cadena.find(caracter)
        while caracter == caracter:
            con_caracter = con_caracter +1
        print(con_caracter)
        
        
        
        
