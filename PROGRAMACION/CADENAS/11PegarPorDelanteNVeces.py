#creo una lista de numero
num = input("Introduce una lista de números: ")
#le pido al usuario que introduzca un número para añadir
añadir = input("Introduce un número para añadir: ")
#pido al usuario cuantas veces quieres añadir el número anterior
numVeces = int(input("Introduce cuantas veces que quieres añadir el número: "))
#añado por delante al número otro número x veces
print(añadir*numVeces+num)