#Mayor y pares. Pide 6 números y guárdalos en una lista. Escribe Mayor: con el mayor, en la posición con su primera posición contando desde 1 y, en otra línea, Pares: con cuántos pares hay.
pares=[]
while len(pares) < 6:
    numero = int(input("Introduce un nº: "))
    pares.append(numero)
mayor = pares[0]
par = 0
posicion = 1
for i in range (len(pares)):
    if pares[i] > mayor:
        mayor = pares[i]
        posicion = i+1
    if pares[i] %2==0:
        par = par +1
print("El número mayor es:",mayor,"y la posicion es:",posicion)
print("Hay:",par,"números pares")