#Pide 6 números y guárdalos en una lista. Escribe cuántos están entre 10 y 20, ambos incluidos.
lista=[]
while len(lista) < 6:
    num = int(input("Introduce un número: "))
    lista.append(num)
cuentan = 0
for num in lista:
    if num >=10 and num <=20:
        cuentan = cuentan +1
print(cuentan)
