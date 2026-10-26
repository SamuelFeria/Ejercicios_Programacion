#Pido al usuario que introduzca un número
num = int(input("Introduce un número: "))
#guardo la variable suma
suma=0
#Compruebo si el número es mayor que 7, si es mayor le pido otro número
if num >7:
    num = int(input("Introduce otro número: "))
    #Recorro los números desde el introducido hasta el 7 imprimiendolos.
for i in range(num,8):
    #imprimo todos los números
    print(i)
    #sumo todos los numeros del recorrido
    suma = num + i
print ("La suma de todos los números es: ",suma)