def numerosPares(lista):
    pares = []
    for numero in lista:
        if numero %2==0:
            pares.append(numero)
    return pares

lista = [1,2,3,4,5,6]
print(numerosPares(lista))