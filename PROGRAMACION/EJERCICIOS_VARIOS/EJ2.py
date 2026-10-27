#Pido al usuario que introduza un número 
num = int(input("Introduce un número: "))
#Compruebo si el número introducido es negativo, si es negativo no calculo el cuadrado
while num >=0:
    #Calcula el cuadrado del número introducido por el usuario
    num = num **2
    print(num)
    num = int(input("Introduce otro número: "))
print("No se puede calcular finalizo programa")


