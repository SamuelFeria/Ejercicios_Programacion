#Construye una función que te imprimirá cada fila invertida.
def posicionInvertida(lista):
    for i in range (len(lista)):
        sublista = lista[i]
        sublista2 = []
        for j in range (len(sublista)-1,-1,-1):
            valor = sublista[j]
            sublista2.append(valor)
        print(sublista2)

listas = [[8,1,6],[3,5,7],[4,9,2]] 
posicionInvertida(listas)
