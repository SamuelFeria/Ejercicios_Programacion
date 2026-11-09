import random

partidas = 0
ganadas_humano = 0
ganadas_maquina = 0
apuestas_par = 0
apuestas_impar = 0
piedras_humano = 0
piedras_maquina = 1      # distintas, para que entre en el bucle la primera vez

while piedras_humano != piedras_maquina:
    # Piedras del jugador (0 a 5)
    piedras_humano = int(input("¿Cuántas piedras quieres mostrar (0 a 5)? "))
    while piedras_humano < 0 or piedras_humano > 5:
        print("Número no válido")
        piedras_humano = int(input("¿Cuántas piedras quieres mostrar (0 a 5)? "))

    # Apuesta del jugador: cualquier cosa distinta de P es impar
    apuesta = input("¿Apuestas par (P) o impar (I)? ")
    match apuesta:
        case "P":
            apuesta_humano = "par"
            apuestas_par = apuestas_par + 1
        case _:
            apuesta_humano = "impar"
            apuestas_impar = apuestas_impar + 1

    # Piedras y apuesta de la máquina
    piedras_maquina = random.randint(0, 5)
    numero = random.randint(1, 2)
    match numero:
        case 1:
            apuesta_maquina = "par"
        case _:
            apuesta_maquina = "impar"

    # Suma total
    suma = piedras_humano + piedras_maquina
    match suma % 2:
        case 0:
            resultado = "par"
        case _:
            resultado = "impar"

    print("La máquina muestra", piedras_maquina, "piedras y apuesta", apuesta_maquina)
    print("La suma total es", suma, "y es", resultado)

    # Ganador de la ronda
    if apuesta_humano == resultado:
        print("Ha ganado el jugador")
        ganadas_humano = ganadas_humano + 1
    else:
        print("Ha ganado la máquina")
        ganadas_maquina = ganadas_maquina + 1

    partidas = partidas + 1

print("fin")

# Estadísticas finales
print("Rondas ganadas por el jugador:", ganadas_humano)
print("Rondas ganadas por la máquina:", ganadas_maquina)
print("Número total de partidas:", partidas)
if apuestas_par > apuestas_impar:
    print("Apuesta humana más frecuente: par")
elif apuestas_impar > apuestas_par:
    print("Apuesta humana más frecuente: impar")
else:
    print("Apuesta humana más frecuente: par e impar por igual")