def calcularMax():
    lista=[]
    while len(lista) < 10:
        num = int(input("Introduce un número: "))
        lista.append(num) 
    max = lista[0] 
    for i in range (1,len(lista)):
        if lista[i] > max:
            max = lista[i]
    return max

calcular = calcularMax()
print(calcular)