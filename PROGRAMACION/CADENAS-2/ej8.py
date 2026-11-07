cadena = input("Introduce una cadena: ")
caracter1 = input("Introduce el primer caracter: ")
caracter2 = input("Introduce el segundo caracter: ")
while len(caracter1) >1:
    print("El primer caracter solo puede conterner 1 valor no más")
    caracter1 = input("Introduce el primer caracter: ")
while len(caracter2) >1:
    print("El segundo caracter solo puede conterner 1 valor no más")
    caracter2 = input("Introduce el segundo caracter: ")
i=0
resultado = ""
while i < (len(cadena)):
    if cadena[i] == caracter1:
        resultado = resultado + caracter2
    else:
        resultado = resultado + cadena[i]
    i = i + 1
print(resultado)