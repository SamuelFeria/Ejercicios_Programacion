def crearMatriz(numero):
    lista = []
    i=1
    while len(lista) < numero:
        lista.append(i)
        i = i+1
    return lista


def crearTabla(n):
    lista = crearMatriz(n)
    for i in range (len(lista)):
        if lista[i] == 1:
            fila2 = n*(1+i)
            lista.append(fila2)
    return lista
            
            
        
num = int(input("Introduce un número: "))
resultadoLista = crearMatriz(num)
print(resultadoLista)
resultadoTabla = crearTabla(num)
print(resultadoTabla)