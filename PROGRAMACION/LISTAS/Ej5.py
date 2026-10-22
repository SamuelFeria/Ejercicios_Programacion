#importamos libreria random
import random

#lista1 vacia
lista1=[]

#lista2 vacia
lista2=[]

#lista3 vacia
lista3=[]

#número de veces que voy a entrar en el for "i" tendrá por defecto valor 0.
for i in range (20):
    
    #genero números randoms entre el 0 y el 100.
    numeroRandom=random.randint(0,100)

    #lista1 con números randoms entre 0 y 100.
    lista1.append(numeroRandom)
    
    #lista2 tendra el cuadrado de los valores de la lista1.
    lista2.append(numeroRandom **2)
    
    #lista3 tendra el cubo de los valores de la lista1.
    lista3.append(numeroRandom **3)
for i in range (20):
#muestra por pantalla el contenido de las 3 listas en tres columnas.
    print(lista1[i], lista2[i], lista3[i])