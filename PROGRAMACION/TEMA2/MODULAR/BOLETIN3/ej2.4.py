#Construye una función que se llame imprimeMatrizInvertida
def imprimeMatrizInvertida(lista):
    for i in range (len(lista)-1,-1,-1):
        sublista = lista[i]
        sublista2 = []
        for j in range(len(sublista)-1,-1,-1):
            valor = sublista[j]
            sublista2.append(valor)
        print(sublista2)
    
listas = [['a','b','c'],  ['d','e','f'], ['g','h','i']] 
imprimeMatrizInvertida(listas)

    