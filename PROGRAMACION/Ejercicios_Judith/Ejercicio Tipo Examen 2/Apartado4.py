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
            print("serie añadida")
            print(lista_valoracion)
            
        case "2":
            if len(lista_titulo)<=0:
                print("No hay series")
            else:
                for i in range (len(lista_titulo)):
                    print(i+1,lista_titulo[i],":",lista_valoracion[i])
                
        case "3":
            total = 0
            suma = 0
            mejor = lista_valoracion[0]
            recomendada = 0
            posicion = 1
            empiezan = "the"
            coinciden = 0
            encontrada = False
            i = 0
            if len(lista_titulo)>0:
                #total
                for i in lista_titulo:
                    total = total +1
                print("Total de series:",total)
                #media
                for i in lista_valoracion:
                    suma = suma + i
                media = suma / len(lista_valoracion)
                print("Valoración media:", media)
                #mejor serie
                for i in range(len(lista_valoracion)):
                    if lista_valoracion[i] > mejor:
                        mejor = lista_valoracion[i]
                        posicion = posicion + i
                print("Mejor serie:","[",lista_titulo[i],"]","(","Posición:",posicion-1,")")
                #recomendada
                for i in range(len(lista_valoracion)):
                    if lista_valoracion[i] >= 8:
                        recomendada = recomendada+1
                print("Recomendadas:",recomendada)
                #empiezan
                for i in range (len(lista_titulo)):
                    if empiezan == lista_titulo[i][0:3]:
                        coinciden = coinciden+1 
                print("Títulos que empiezan por The:",coinciden)
                #floja
                while i < len(lista_valoracion) and encontrada == False:
                    if lista_valoracion[i] < 5:
                        encontrada = True 
                    else:
                        i = i +1

                if encontrada:
                    print("Primera seria floja:", lista_titulo[i])
                else:
                   print("Primera serie floja: ninguna") 

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



