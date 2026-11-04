#pido un número en forma de cadena
num = (input("Introduce un número: "))
#pido que valores de la cadena quiere quitar
quitar = int(input("Introduce la cantidad de números que deseas quitar: "))
#indico como quitar los valores de la cadena por la derecha
print (num[:-(quitar)])