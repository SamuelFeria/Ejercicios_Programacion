#pide un dia
dia = int(input("Introduce un día: "))
#pide un mes
mes = int(input("Introduce un mes: "))
#pide un año
anho = int(input("Introduce un año: "))
#si dia es mayor a 31 dia incorrecto
while dia > 31:
    print("Día incorrecto")
    dia = int(input("Vuelve a introducir un día: "))

listaDias=[31,28,31,30,31,30,31,31,30,31,30,31]
#si mes es mayor que la longitud de la lista incorrecto
while mes > len(listaDias):
    print("Mes incorrecto")
    mes = int(input("Introduce otro mes: "))
for i in range(len(listaDias)):
    diasTrancurridos = (listaDias[0]+listaDias[-1]) - dia

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
print("Han trasncurrido: ",diasTrancurridos, "dias.")
print("¿",anho, "es bisisesto?", bisiesto )