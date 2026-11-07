#Pide 6 números y guárdalos en una lista. Crea una nueva lista solo con los pares y escríbela.
lista=[]
while len(lista) < 6:
    num = int(input("Introduce un número: "))
    lista.append(num)
lista_pares=[]
for num in lista:
    if num %2==0:
        lista_pares.append(num)
print(lista_pares)
