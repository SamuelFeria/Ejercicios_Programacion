#lista vacia
lista=[]
#numero de veces que voy a entrar en el for "i" tendrá por defecto valor 0.
for i in range (10):
    #pido al usuario que introduzca un número por teclado.
    numero = int(input("Introduce un nº: "))
    #guardo el número en la lista.
    lista.append(numero)
    #muestro por pantalla la lista completa.
print("La lista completa es: ", lista)
numMin = lista[0]
numMax = lista[0]
#comparo los valores de la lista para ver cual es el mínimo y cual es el máximo.
for i in range (1,len(lista)):
    #si el valor de la lista es menor que el mínimo guardado, actualizo el mínimo.
    if lista[i] < numMin:
        numMin = lista[i]
    #si el valor de la lista es mayor que el máximo guardado, actualizo el máximo.
    elif lista[i] > numMax:
        numMax = lista[i]
#muestro por pantalla el numero minimo y el maximo actualizado.
print("El número mínimo es: ", numMin, "y el número máximo es: ", numMax)