#Creo una lista vacia
lista = []
#Pido al usuario que introduzca 15 números.
for i in range(15):
    numero = int(input("Introduce un número: "))
    #guardo esos numeros en la lista
    lista.append(numero)

numero = int(input("Introduce numero: "))
#Compruebo que el número introducido sea mayor o igual que 0
# y menor que la longitud de la lista
while numero < 0 or numero >= len(lista):
    numero = int(input("El numero debe ser menor que 15. Introduce otro numero: "))
#Repito el desplazamiento tantas veces como indique el usuario
for vuelta in range(numero):
     # Guardo el último número de la lista para no perderlo
    ultimo = lista[-1]
    # Recorro la lista desde el final hasta la segunda posición
    # y desplazo cada número una posición hacia la derecha
    for i in range (len(lista)-1, 0, -1):
        lista[i] = lista[i - 1]
    # Coloco el último número guardado al principio de la lista
    lista[0] = ultimo
# Muestro la lista con los números ya desplazados
print(lista)