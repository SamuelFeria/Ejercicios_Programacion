print("==============")
print("MI CATÁLOGO DE SERIES")
print("==============")
print("Elige [1] para añadir serie")
print("Elige [2] para mostrar el listado de tus series ")
print("Elige [3] para mostar estadísticas")
menu = input("Elige una opción. Para salir, escirbe 'salir'... ").lower()
lista_titulo=[]
lista_valoracion=[]
while menu != "salir":
    match menu:
        case "1":

            titulo = input("Introduce el título de la serie: ")
            while titulo =="":
                print("tiutlo incorrecto")
                titulo = input("Introduce el título de la serie: ")
            lista_titulo.append(titulo)
            print(lista_titulo)

            valoracion = float(input("Introduce la valoracion: "))
            while valoracion <0 or valoracion > 10:
                print("valoracion incorrecta")
                valoracion = float(input("Introduce la valoracion: "))
            lista_valoracion.append(valoracion)
            print(lista_valoracion)
            print("serie añadida")

        case "2":
            
            if len(lista_titulo)<=0:
                print("No hay series")
            else:
                for i in range (len(lista_titulo)):
                    print(i+1,lista_titulo[i],":",lista_valoracion[i])

        case "3":
            print("Ejecutando estadísticas")
        case _:
            print("Opción incorrecta")
    print("==============")
    print("MI CATÁLOGO DE SERIES")
    print("==============")
    print("Elige [1] para añadir serie")
    print("Elige [2] para mostrar el listado de tus series ")
    print("Elige [3] para mostar estadísticas")
    menu = input("Elige una opción. Para salir, escirbe 'salir'... ")
print("Hasta la próxima")



