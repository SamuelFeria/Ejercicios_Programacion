#pido un año
anho = int(input("Introduce un año: "))
#si año es negativo pido otro año
while anho <0:
    print("Año incorrecto")
    anho = int(input("Vuelve a introducir un año: "))
#bisiesto por defecto en falso
bisiesto = False
#si es divisible por 4 es bisiesto
if anho %4==0:
    bisiesto = True
#si es divisible por 100 no es bisiesto
if anho %100==0:
    bisiesto = False
#si es divisible por 400 es bisiesto
if anho %400==0:
    bisiesto = True
print("¿Es bisiesto?", bisiesto)