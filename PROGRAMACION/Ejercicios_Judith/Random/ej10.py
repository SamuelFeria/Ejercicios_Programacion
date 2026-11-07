#Simula 5 lanzamientos de una moneda (0 es cara y 1 es cruz) y escribe cuántas caras han salido.
import random
cara=0
for i in range(5):
    moneda = random.randint(0,1)
    if moneda ==0:
        cara = cara +1
print("Cara ha salido:", cara,"veces")
