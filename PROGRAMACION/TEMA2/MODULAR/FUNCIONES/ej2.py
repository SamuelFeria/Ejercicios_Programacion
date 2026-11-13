def esMultiplo(num1,num2):
    multiplo = False
    if num1 % num2 == 0:
        multiplo = True
        
    return multiplo
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce un número: "))

multiplos = esMultiplo(num1,num2)
print(multiplos)