num= int(input("Introduce un número: "))
lista=[]
while num !=0: 
    num = int(input("Introduce un número: "))
    lista.append(num)
    for i in range(len(lista-1)):  
        if len(lista)!=1:
            lista[-1] > lista[-2]
            print ("Creciente")
        else:
            print("Decreciente", "Desordenado")
   