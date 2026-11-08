#suma. Pide suma hasta que se escriba 999. Las suma válidas están entre -50 y 60, ambas incluidas; si no, escribe Temperatura no válida y sigue pidiendo (esa no cuenta). Al terminar escribe Máxima: , Mínima: y Media: (una por línea) con las válidas, o No hay suma si no se escribió ninguna válida.
temperatura = int(input("Introduce una temperatura: ")) 
maxima = 0
minima = 0
media = 0
contador = 0
suma = 0
while temperatura !=999:
    if temperatura >= -50 and temperatura <= 60:
        print("Temperatura válida")
        if contador == 0:
            maxima = temperatura
            minima = temperatura
        else:
            if temperatura > maxima:
                maxima = temperatura
            elif temperatura < minima:
                minima = temperatura
        suma = suma + temperatura
        contador = contador +1  

    else :
        print("Temperatura no válida")
    temperatura = int(input("Introduce una temperatura: "))

if contador == 0:
    print("No hay temperatura")
    
else:
    media = suma /contador
    print("Máxima:",maxima,"Minima",minima,"Media:",media)