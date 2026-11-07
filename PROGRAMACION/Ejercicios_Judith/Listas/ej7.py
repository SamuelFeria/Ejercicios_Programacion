#Pide 5 números y guárdalos en una lista. Cambia por 0 los que sean negativos, modificando la propia lista por posiciones, y escribe la lista.
lista=[]
while len(lista) < 5:
    num = int(input("Introduce un número: "))
    lista.append(num)
negativo = 0
for i in range (len(lista)):
    if lista[i] < 0:
        lista[i]= negativo
print(lista)