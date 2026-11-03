#pido un número por telcado
num = int(input("Introduce un número: "))
#creo resultado que empieza en 0
resultado = 0
#por defecto negativo es falso
negativo = False
#si es negativo, me lo guardo y lo paso a positivo
if num < 0:
    negativo = True
    num = num*-1
#mientras que el número sea distinto de 0
while num !=0:
    #cojo la ultima cifra del número
    UltimaCifra = num %10
    #al resultado le multiplico por 10 y le suma esa cifra, para poder añadirla
    resultado = resultado *10 + UltimaCifra
    #quito la ultima cifra del número
    num = num //10
#si el numero es negativo le cambio el signo al resultado
if negativo == True:
    resultado = resultado * -1
#muestro el resultado 
print(resultado)