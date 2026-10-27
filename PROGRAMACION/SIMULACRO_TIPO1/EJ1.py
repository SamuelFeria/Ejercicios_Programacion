lista=[]
#Diseña y escribe  un programa Python que permita introducir grupos de 3 números.
for i in range (3):
  num=int(input("introduce un número: "))
  lista.append(num)
#El programa acaba cuando introduzca 0 0 0, escribe fin
while lista != [0,0,0]:
 
  if lista [0] <= lista [1] and lista[1] <= lista[2]:
    print(lista, "creciente")
  elif lista [0] >= lista [1] and lista[1] >= lista[2]:
    print(lista, "decreciente")
  else:
    print(lista, "desordenados")

  lista=[]
  for i in range(3):
    num=int(input("introduce un número: "))
    lista.append(num)
print("FIN")








#Si Los números han seguido un orden creciente, en ese caso imprime “creciente”.

#si los números han seguido un orden decreciente  (de mayor a menor), , en ese caso imprime “decreciente”.
#si no sigue orden creciente o decreciente imprimirá la palabra “desordenados”

  

