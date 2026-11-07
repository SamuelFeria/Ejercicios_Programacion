#Pide 6 números y guárdalos en una lista. Escribe cuántos son mayores que 10.
lista=[]
while len(lista) < 6:
    num = int(input("Introduce un número: "))
    lista.append(num)
mayores=0
for num in lista:
    if num > 10:
        mayores = mayores +1
print(mayores)
