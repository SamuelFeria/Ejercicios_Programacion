def sumaFila(lista):
    suma = 0
    for num in lista:
        suma = suma + num
    return suma
        
listaNums = []
numero = int(input("Introduce un numero: "))
listaNums.append(numero)
numero2 = int(input("Introduce un numero: "))
listaNums.append(numero2)
numero3 = int(input("Introduce un numero: "))
listaNums.append(numero3)
resultado = sumaFila(listaNums)
print(resultado)