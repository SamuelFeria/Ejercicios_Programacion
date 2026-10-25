lista=[]
#pido al usuario que introduzca 15 numeros para almacenar en una lista.
for i in range(15):
    numero = int(input("introduce un número: "))
    lista.append(numero)
#guardo el ultimo valor de la lista
ultimo = lista[-1]
# Desplazo los elementos hacia la derecha
for i in range (14,0,-1):
    lista[i] = lista[i-1]
# Coloco el último elemento en la primera posición
lista[0] = ultimo
    
print(lista)



    