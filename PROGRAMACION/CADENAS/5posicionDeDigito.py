#Pido un número entero 
num = input("Introduce un número: ")
#pido el valor a buscar dentro del número
ocurrencia = (input("introduce una ocurrencia: "))
#recorro la lista y devuelvo la posicion de ocurrencia si es que la hay, sino devuelvo -1
for i in range (len(num)):
    if num[i] == ocurrencia:
        ocurrencia = num[i]
        print (ocurrencia)
    else:
        print(-1)


