#Configuramos el menu para que el usuario pueda elegir
print("==========MENU=============")
print("Introduzca 1 si desea ver carácter a carácter...")
print("introduzca 2 si desea saber el '%' de veces que aparece el carácter en una cadena...")
print("Escriba exit si desea salir...")
#pide al usuario que elige un menú
menu = input("Elige a que opción desea ingresar... ")
#mientras menu sea disinto de exit
while menu != "exit":
#si elige el 1
    match menu:
        case "1":
            print("Has seleccionado la opción 1 del menú.")
            #pide una cadena por teclado y escribe por pantalla cada caracter de una cadena introducida por teclado
            cadena = input("Introduce una cadena: ")
            for i in range (len(cadena)):
                caracterCadena = cadena[i]
                print(caracterCadena)
        #si elige el 2
        case "2":
            print("Has seleccionado la opción 2 del menú.")
            #te pide un caracter por teclado y el sistema contara el % de veces que aparece ese caracter que se ha introducido por teclado
            cadena = input("introduce una cadena: ").upper()
            caracter = input("introduce un caracter: ").upper()
        #si elige exit
        case "exit":
            print("Fin del programa")
        case _:
            print("Valor incorrecto, vuelve a introducir un valor...")
            print("==========MENU=============")
            print("Introduzca 1 si desea ver carácter a carácter...")
            print("introduzca 2 si desea saber el '%' de veces que aparece el carácter en una cadena...")
            print("Escriba exit si desea salir...")
       

   
        
        
       
        
