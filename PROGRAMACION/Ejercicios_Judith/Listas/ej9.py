#Pide 5 números y guárdalos en una lista. Crea una nueva lista con los mismos números en orden inverso y escríbela. Sin reverse.
lista=[]
while len(lista) < 5:
    num = int(input("Introduce un número: "))
    lista.append(num)
lista2=[]
for i in range (len(lista)-1,-1,-1):
    lista2.append(lista[i])
print(lista2)

