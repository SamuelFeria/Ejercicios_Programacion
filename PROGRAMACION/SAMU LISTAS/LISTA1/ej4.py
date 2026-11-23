#Pares e impares: a partir de una lista de números, crea dos listas nuevas, una solo con los pares y otra solo con los impares, y muéstralas.
lista_numeros = []
lista_pares = []
lista_impares = []
for i in range (6):
    numero = int(input("Introduce un numero: "))
    lista_numeros.append(numero)
for numeros in lista_numeros:
    if numeros %2==0:
        lista_pares.append(numeros)
    else:
        lista_impares.append(numeros)
print("Pares:",lista_pares,"impares:",lista_impares)