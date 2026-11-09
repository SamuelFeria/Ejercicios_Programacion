import random

vidaHeroe = 50
vidaVillano = 50

fuerza = int(input("Fuerza del ataque (1 a 3): "))
while fuerza < 1 or fuerza > 3:
    fuerza = int(input("Fuerza incorrecta, introduce de 1 a 3: "))

dadoHeroe = random.randint(1, 6)
dadoVillano = random.randint(1, 6)

danoHeroe = dadoHeroe * fuerza
danoVillano = dadoVillano

vidaHeroe = vidaHeroe - danoVillano
vidaVillano = vidaVillano - danoHeroe

print("Daño del héroe: " + str(danoHeroe))
print("Daño del villano: " + str(danoVillano))
print("Vida del héroe: " + str(vidaHeroe))
print("Vida del villano: " + str(vidaVillano))

if danoHeroe > danoVillano:
    print("Ha hecho más daño el héroe")
elif danoVillano > danoHeroe:
    print("Ha hecho más daño el villano")
else:
    print("Empate")