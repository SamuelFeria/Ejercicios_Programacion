def devolverFilaYColumna(lista,numFila,numColumna):
   
   resultadoFilaYColumna = lista[numFila][numColumna]
   return resultadoFilaYColumna
   """if numFila == 0 and numColumna == 0:
        filaYColumna = lista[0][0]
        return [filaYColumna]
   elif numFila == 0 and numColumna == 1:
        filaYColumna = lista[0][1]
        return [filaYColumna]
   elif numFila == 0 and numColumna == 2:0
        filaYColumna = lista[0][2]
        return [filaYColumna]
   elif numFila == 1 and numColumna == 0:
        filaYColumna = lista[1][0]
        return [filaYColumna]
   elif numFila == 1 and numColumna == 1:
        filaYColumna = lista[1][1]
        return [filaYColumna]
   elif numFila == 1 and numColumna == 2:
        filaYColumna = lista[1][2]
        return [filaYColumna]
   elif numFila == 2 and numColumna == 0:
        filaYColumna = lista[2][0]
        return [filaYColumna]
   elif numFila == 2 and numColumna == 1:
        filaYColumna = lista[2][1]
        return [filaYColumna]
   elif numFila == 2 and numColumna == 2:
        filaYColumna = lista[2][2]
        return [[filaYColumna]]"""

lista = [[8,1,6],[3,5,7],[4,9,2]]
numFila = int(input("Introduce un numero de fila: "))
numColumna = int(input("Introduce un numero de columna: "))

resFilaYColumna = devolverFilaYColumna(lista,numFila,numColumna)
print(resFilaYColumna)
