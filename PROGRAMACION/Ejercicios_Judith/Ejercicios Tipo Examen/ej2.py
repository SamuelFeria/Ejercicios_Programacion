#Adivina el número. El programa elige un número al azar entre 1 y 20. El usuario va escribiendo números hasta acertar. Si se queda corto, escribe El número es mayor; si se pasa, El número es menor. Al acertar, escribe Acertado en seguido del número de intentos y intentos.
import random

numero_elegido = random.randint(1,20)
adivina= 0
intentos = 0

while adivina != numero_elegido:
    adivina = int(input("Introduce un número: "))
    intentos = intentos+1
    if adivina < numero_elegido:
        print("El número es mayor")
    elif adivina > numero_elegido:
        print("El número es menor")
        
print("Has acertado","y los intentos han sido:",intentos)
