#lista vacía.
lista=[]
#i es un contador con valor 0, para contar las vueltas que tiene que dar.
i=0
#introduce un número por teclado.
numero = int(input("Introduce un nº: "))
for i in range(10):
    #mientras que la lista tenga menos de 10 valores añade un valor más.
    if len(lista) < 10 :
        #guardar numero en lista.
        lista.append(numero)
        #introduce otro número por teclado.
        numero = int(input("Introduce otro nº: "))
 #imprime la lista completa empezando por el último valor [9:0]. [posición inicial : posicón final : empiezo por el final]  
print(lista [len(lista)::-1])

 