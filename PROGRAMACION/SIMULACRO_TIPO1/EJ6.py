#pide un dia
dia = int(input("Introduce un día: "))
#pide un mes
mes = input("Introduce un mes: ")
#puide un año
anho = int(input("Introduce un año: "))
while dia > 31:
    print("Día incorrecto")
    dia = int(input("Vuelve a introducir un día: "))
listaDias=[31,28,31,30,31,30,31,31,30,31,30,31]
diasTrancurridos = listaDias[0] - dia
print("Han trasncurrido: ",diasTrancurridos, "dias.")