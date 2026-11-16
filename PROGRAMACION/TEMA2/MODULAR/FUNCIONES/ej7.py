def calcularMaxMin(max,min):
    
    max = lista[0] 
    min = lista[0]
    for i in range (1,len(lista)):
        if lista[i] > max:
            max = lista[i]
        if lista[i] < min:
            min = lista[i]
    return [max,min]
   
lista=[]
while len(lista) < 10:
        num = int(input("Introduce un número: "))
        lista.append(num) 
calcular = calcularMaxMin(max,min)
print(calcular)
