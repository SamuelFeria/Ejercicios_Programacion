"""Construye una función que recorra esta lista e imprima cada sublista (fila).  
Por ejemplo, para los valores anteriores el programa debe imprimir:"""
def recorrerLista(lista):
    for i in range (len(lista)):
        valor = lista[i]
        print(valor)


listas = [[8,1,6],[3,5,7],[4,9,2]]  
recorrerLista(listas)

   
    