#Construye una función que te imprima por filas comenzando por la última
def imprimirFilas(lista):
    for i in range(len(lista)-1,-1,-1):
        ultimaFila = lista[i]
        print(ultimaFila)

listas = [[8,1,6],[3,5,7],[4,9,2]] 
imprimirFilas(listas)