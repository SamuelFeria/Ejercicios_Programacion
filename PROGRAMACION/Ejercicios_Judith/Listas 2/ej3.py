#Puntuaciones (listas): pide 6 puntuaciones de un videojuego, guárdalas en una lista y muestra la mayor, la menor y la media.
lista_puntuaciones = []
suma = 0
while len(lista_puntuaciones) < 6:
    puntuacion = int(input("Introduce la puntuación: "))
    lista_puntuaciones.append(puntuacion)
mayor = lista_puntuaciones[0]
menor = lista_puntuaciones[0]
for i in range(len(lista_puntuaciones)):
    suma = lista_puntuaciones[i] + suma 
    media = suma / len(lista_puntuaciones)
for i in range(len(lista_puntuaciones)):
    if lista_puntuaciones[i] < menor:
        menor = lista_puntuaciones[i]
    if lista_puntuaciones[i] > mayor:
        mayor = lista_puntuaciones[i]

print("La puntiación mayor es:",mayor,"|","la puntuación menor es:",menor,"|","la media es:",media)