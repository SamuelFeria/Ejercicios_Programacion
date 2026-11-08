#Menú de números. Menú con estas opciones:
#Añadir número
#Mostrar lista
#Mostrar media
#Salir
#Opción 1: pide un número y lo añade a una lista.
#Opción 2: escribe la lista con print(lista).
#Opción 3: escribe Media: con la media, o No hay números si la lista está vacía.
#Cualquier otra: Opción incorrecta.
#Al salir: escribe Fin.
menu=""
lista=[]

while menu != "salir":
    print("======MENÚ======")
    print("Escribe 1 y pulsa enter si queires añadir un número...")
    print("Escribe 2 y pulsa enter si queires ver la lista...")
    print("Escribe 3 y pulsa enter si queires ver la media...")
    print("Si quieres salir escribe 'salir' y pulsa enter...")
    menu=input("Escribe la opción del menú que desees: ")

    match menu:
        case "1":
            numero=int(input("Escribe un nº: "))
            lista.append(numero)
        case "2":
                print(lista)
        case "3":
            if len(lista)==0:
                print("No hay números para calcular la media")
            else:
                suma = 0
                for i in lista:
                    suma = suma + i
                media = suma / len(lista)
                print("La media es", media)
        case "salir":
            print("Fin")
        case _:
            print("Opción no válida")




