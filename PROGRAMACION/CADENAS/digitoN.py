#Pido el número por teclado
num = int(input("Introduce un número:"))
# Pido la posición n por teclado
posicion = int(input("introduce una posición: "))
#creo una copia el número para no pererlo
copia = num
#creo un contador que empieza en 0
numDigitos = 0
# Cuento cuántas cifras tiene el número 
while copia !=0:
    #sumo 1 al contador de cifras
    numDigitos = numDigitos+1
    #quito la ultima cifra de la copia
    copia = copia //10
# Calculo cuántas cifras tengo que quitar por la derecha: total - 1 - n
quitar = numDigitos -1 -posicion
#creo un contador para saber cuantas veces he quitado la cifra
contador = 0
# Repito esas veces: quito la última cifra del número
while contador < quitar:
    # Cojo la última cifra de lo que queda (con % 10)
    num = num //10
    #sumo 1 al contador
    contador = contador + 1
# Muestro el resultado
print(num%10)