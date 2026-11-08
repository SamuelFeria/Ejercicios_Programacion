#Lista de 8. Pide 8 números y guárdalos en una lista. Escribe Mayores que la media: con cuántos números son mayores que la media y, en otra línea, Menor: con el menor, en la posición con su primera posición contando desde 1.
lista=[]
suma=0
media=0
mayores=0
posicion = 1
while len(lista)<8:
    numero=int(input("Introduce un numero: "))
    lista.append(numero)
menores = lista[0]
for i in lista:
    suma = suma + i
media = suma / len(lista)
for i in lista:
    if i > media:
        mayores = mayores +1
for i in range(len(lista)):
    if lista[i] < menores:
        menores = lista[i]
        posicion = i + 1
print("Mayores:", mayores)
print("Menores:",menores,"y su posicion:",posicion)

