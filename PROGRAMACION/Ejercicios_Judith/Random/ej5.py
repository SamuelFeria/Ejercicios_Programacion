#Genera números aleatorios entre 1 y 100 hasta que salga uno mayor que 90. Escribe cuántos números han salido (incluido el mayor que 90).
import random
numero_random=random.randint(1,100)
numero_generado=1
while numero_random <=90:
    numero_random=random.randint(1,100)
    numero_generado= numero_generado+1
print("Han saldio:",numero_generado,"números")