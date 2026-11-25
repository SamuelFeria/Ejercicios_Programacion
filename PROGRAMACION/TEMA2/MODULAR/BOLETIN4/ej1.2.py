def devolverFilaCompleta(lista,numFila):
   resultadoFila =  lista[numFila] 
   return resultadoFila

lista = [[8,1,6],[3,5,7],[4,9,2]]
numFila = int(input("Introduce un numero de fila: "))
resFilaCompleta = devolverFilaCompleta(lista,numFila)
print(resFilaCompleta)