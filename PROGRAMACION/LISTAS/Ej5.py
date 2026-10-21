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
lista2.append(lista1 **2)
#lista3 tendra el cubo de los valores de la lista1.
lista3.append(lista1 **3)
#muestro la lista1 de números randoms.
print(lista1)
#muestro la lista2. 
print(lista2)
#muestro la lista 3.
print(lista3)
#muestra por pantalla el contenido de las 3 listas en tres columnas.
print(lista1, lista2, lista3)