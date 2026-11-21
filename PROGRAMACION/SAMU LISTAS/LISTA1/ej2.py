#Mayor y menor: dada una lista de números que escribe el usuario, muestra cuál es el valor más grande y cuál es el más pequeño.
lista_numeros = []

while len(lista_numeros) < 6:
    numero = int(input("Introduce nº: "))
    lista_numeros.append(numero)

mayor = lista_numeros[0]
menor = lista_numeros[0]
for i in range(len(lista_numeros)):
    if lista_numeros[i] > mayor:
        mayor = lista_numeros[i] 
    elif lista_numeros[i] < menor:
        menor = lista_numeros[i]

print("El mayor es:",mayor,"y el menor es:",menor)
