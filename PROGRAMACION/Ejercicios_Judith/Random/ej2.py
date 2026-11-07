#Tira un dado 10 veces (números aleatorios entre 1 y 6) y escribe cuántas veces ha salido el 6.
import random
contador=0
for i in range (10):
    dado = random.randint(1,6)  
    print(dado)
    if dado == 6:
        contador = contador +1
print("El 6 ha salido: ",contador)
