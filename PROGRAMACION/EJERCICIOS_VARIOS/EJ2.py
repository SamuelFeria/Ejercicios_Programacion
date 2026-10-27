#Pido al usuario que introduza un número 
num = int(input("Introduce un número: "))
#Compruebo si el número introducido es negativo, si es negativo no calculo el cuadrado
if num > 0:
    #Calcula el cuadrado del número introducido por el usuario
    num= num**2
if num <0:
    print("No se puede calcular finalizo programa")
print(num)

