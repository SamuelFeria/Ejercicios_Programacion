import random

nombre = ""
total_alumnos = 0
total_gryffindor = 0
total_slytherin = 0
total_hufflepuff = 0
total_ravenclaw = 0

while nombre != "voldemort":
    print("=========================")
    print("SOMBRERO SELECCIONADOR")
    print("=========================")
    print("1. Seleccionar casa para un alumno")
    print("2. Mostrar estadísticas")
    menu = input("Elige una opción. Si quieres salir del programa, escribe la opción 1 y el nombre del personaje innombrable: ")

    match menu:
        case "1":
            nombre = input("Introduce el nombre del alumno: ").lower()
            if nombre != "voldemort":
                numero = random.randint(1, 4)
                if numero == 1:
                    casa = "Gryffindor"
                    total_gryffindor = total_gryffindor + 1
                elif numero == 2:
                    casa = "Slytherin"
                    total_slytherin = total_slytherin + 1
                elif numero == 3:
                    casa = "Hufflepuff"
                    total_hufflepuff = total_hufflepuff + 1
                else:
                    casa = "Ravenclaw"
                    total_ravenclaw = total_ravenclaw + 1
                total_alumnos = total_alumnos + 1
                print("El Sombrero dice que", nombre, "pertenece a", casa)

        case "2":
            if total_alumnos > 0:
                print("Total de alumnos:", total_alumnos)
                print("Gryffindor:", total_gryffindor)
                print("Slytherin:", total_slytherin)
                print("Hufflepuff:", total_hufflepuff)
                print("Ravenclaw:", total_ravenclaw)

        case _:
            print("Opción incorrecta")

print("Apparition, transpórtame a otro sitio")