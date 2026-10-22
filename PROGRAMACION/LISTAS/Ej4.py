#lista vacía.
lista=[]

#i es un contador con valor 0, para contar las vueltas que tiene que dar.
i=0

#mientras que la lista tenga menos de 10 valores añade un valor más.
for i in range(10):
    
    #introduce un número por teclado.
    numero = int(input("Introduce un nº: "))  
    #guardar numero en lista.
    lista.append(numero)
         
 #imprime la lista completa empezando por el último valor [9:0]. [posición inicial : posicón final : empiezo por el final]  
print(lista [len(lista)::-1])

 