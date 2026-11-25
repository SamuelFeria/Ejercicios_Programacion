def sumaElementosMatriz(lista):
    suma = 0
    for numero in lista:
        suma = suma + numero
    return suma

lista = [1,2,3,4,5]
print(sumaElementosMatriz(lista))