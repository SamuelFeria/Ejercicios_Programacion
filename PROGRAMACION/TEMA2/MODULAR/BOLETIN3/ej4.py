def  estaOrdenadaAscendemente(lista):
    asc = True
    i = 0 
    while asc and i < len(lista):
        
        if lista[i] >= lista[i+1]:
            asc = False
        else:
            i = i + 1
        
    return asc

lista = [1,2,3,3,7,9,15]
resultado = estaOrdenadaAscendemente(lista)
print (resultado)