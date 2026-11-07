#Pide 5 números y guárdalos en una lista. Crea una nueva lista con cada número multiplicado por 2 y escríbela.
lista=[]
while len(lista) < 5:
    num = int(input("Introduce un número: "))
    lista.append(num)
lista2=[]
for num in lista:
    num = num * 2
    lista2.append(num)
print(lista2)