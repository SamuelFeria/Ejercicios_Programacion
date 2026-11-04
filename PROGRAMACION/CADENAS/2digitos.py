"""#Pido un número por teclado.
num = int(input("Introduce un número: "))
#creo un contador que empieza en 0
numDigitos = 0
#si el número es negativo, lo multiplico por -1 para hacerlo positivo.
if num <0:
    num = num * -1
#si el numero es 0, el contador es 1 
#elif 
if num == 0:
    numDigitos = 1
    #Mientras el numero sea distinto de 0:
else:
    while num !=0:
        #sumo 1 al contador
        numDigitos = numDigitos + 1
        #quito la ultima cifra del numero 
        num = num //10
#cuando el bucle termina, muestro el resultado
print(numDigitos)"""

cadena = input("introduce una cadena que empiece por A: ").upper()
while cadena[0] != "A":
    cadena = input("introduce una cadena que empiece por A: ").upper()
print(cadena)
    

