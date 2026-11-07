#Pide 5 números y guárdalos en una lista. Recorre la lista y escribe la suma de sus elementos (sin sum).
lista=[]
while len(lista) < 5:
    num = int(input("Introduce un número: "))
    lista.append(num)
suma = 0
for num in lista:
    suma = suma + num
print(suma)