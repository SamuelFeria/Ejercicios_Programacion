#Suma de elementos: pide al usuario cinco números enteros, guárdalos en una lista y muestra la suma de todos ellos.
lista_numero = []
i = 0
while i <=4:
    numero = int(input("Introduce un número: "))
    lista_numero.append(numero)
    i = i + 1
suma = 0
for j in range(len(lista_numero)):
    suma = suma + lista_numero[j]
print(suma)

