def calculaMayorQueNum(lista,numero):
    lista2 = []
    for i in range(len(lista)):
        if lista[i] > numero:
            numero = lista[i]
            lista2.append(numero)
    return lista2

lista = [1,2,3,4,5,6,7,8,9]
num = int(input("introduce un número: "))
operacion = calculaMayorQueNum(lista,num)
print(operacion)