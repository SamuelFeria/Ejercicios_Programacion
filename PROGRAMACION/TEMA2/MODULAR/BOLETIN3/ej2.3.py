#Construye una función que te imprimirá cada fila invertida.
def posicionInvertida(lista):
    for i in range (len(lista)):
        fila = lista[i]
        sublista2 = []
        for j in range (len(fila)-1,-1,-1):
            valor = fila[j]
            sublista2.append(valor)
        print(sublista2)

listas = [[8,1,6],[3,5,7],[4,9,2]] 
posicionInvertida(listas)
