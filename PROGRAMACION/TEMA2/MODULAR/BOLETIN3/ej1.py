def ordenInverso(lista):
    lista_inversa = []
    for i in range (len(lista_num)-1,-1,-1):
        lista_inversa.append(lista_num[i])
    return lista_inversa

lista_num = []
numVeces = int(input("Introduce el nº de veces que desea introducir un número: "))
for i in range (numVeces):
    num = int(input("Introduce el número: "))
    lista_num.append(num)
print (ordenInverso(lista_num))

