#Dos dados. Lanza dos dados al azar, una y otra vez, hasta que sumen 7. En cada lanzamiento escribe Dados: seguido del valor del primero, y y el valor del segundo. Al terminar escribe Han hecho falta con el número de lanzamientos y lanzamientos.
import random
suma = 0
contador = 0
while suma !=7:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
    print(dado1,"y",dado2)
    contador = contador +1
print("El resultado es:",dado1,"+",dado2,"=",suma,"y se han lanzado",contador,"veces")