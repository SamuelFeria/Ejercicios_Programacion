#Ahora construye una función dameColumna que dada una matriz y un número de columna, 
#me devuelva la lista de los elementos de esa columna.
def dameColumna (lista):
    for i in range(len(lista)):
        sublista = lista[i]
        sublista2 = []
        for j in range (len(sublista)):
             
            if dame_columna == 0:
                valor = sublista[j]
                sublista2.append(valor)
                return sublista2
            elif dame_columna == 1:
                valor2 = sublista[1]
                sublista2.append(valor2)
                return sublista2
            elif dame_columna == 2:
                valor3 = sublista[2]
                sublista2.append(valor3)
                return sublista2
       

listas = [['a','b','c'],  ['d','e','f'], ['g','h','i']]
dame_columna = int(input("Introduce la columna de 0 a 2: "))
resultado = dameColumna(listas)
print(resultado)