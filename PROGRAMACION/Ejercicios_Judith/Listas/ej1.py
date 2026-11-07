#Pide 5 números y guárdalos en una lista. Escribe la lista, su primer elemento y su último elemento.
lista=[]
while len(lista) < 5:
    num = (input("Introduce un número: "))
    lista.append(num)
print(lista, lista[0], lista[-1]) 