#Tira dos dados hasta que sumen 7. Escribe cuántas tiradas han hecho falta.
import random
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2
tirada = 1
while suma != 7:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
    tirada = tirada + 1
    print(suma)
print("Se han necesitado:",tirada,"tiradas")

