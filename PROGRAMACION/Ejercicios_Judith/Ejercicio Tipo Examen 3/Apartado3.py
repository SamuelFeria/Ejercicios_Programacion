import random

vidaHeroe = 50
vidaVillano = 50
turnos = 0
danoTotalHeroe = 0
golpeMasFuerte = 0
turnoGolpe = 0
turnosVillanoMas = 0

while vidaHeroe > 0 and vidaVillano > 0:
    turnos = turnos + 1

    fuerza = int(input("Fuerza del ataque (1 a 3): "))
    while fuerza < 1 or fuerza > 3:
        fuerza = int(input("Fuerza incorrecta, introduce de 1 a 3: "))

    dadoHeroe = random.randint(1, 6)
    dadoVillano = random.randint(1, 6)

    danoHeroe = dadoHeroe * fuerza
    danoVillano = dadoVillano

    vidaHeroe = vidaHeroe - danoVillano
    vidaVillano = vidaVillano - danoHeroe

    if vidaHeroe < 0:
        vidaHeroe = 0
    if vidaVillano < 0:
        vidaVillano = 0

    danoTotalHeroe = danoTotalHeroe + danoHeroe
    if danoHeroe > golpeMasFuerte:
        golpeMasFuerte = danoHeroe
        turnoGolpe = turnos
    if danoVillano > danoHeroe:
        turnosVillanoMas = turnosVillanoMas + 1

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

if vidaHeroe == 0 and vidaVillano == 0:
    print("Empate")
elif vidaVillano == 0:
    print("Gana el héroe")
else:
    print("Gana el villano")

print("Turnos jugados: " + str(turnos))
print("Daño total del héroe: " + str(danoTotalHeroe))
print("Golpe más fuerte del héroe: " + str(golpeMasFuerte) + " (turno " + str(turnoGolpe) + ")")
print("Turnos en los que el villano hizo más daño: " + str(turnosVillanoMas))