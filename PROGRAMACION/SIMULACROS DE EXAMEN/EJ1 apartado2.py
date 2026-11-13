
print("=========================")
print("SOMBRERO SELECCIONADOR")
print("=========================")
print("Pulsa [1] para seleccionar casa para un alumno")
print("Pulsa [2] para mostar estadísticas")
menu = input("Introduce un número del menú y pusla enter...")
while menu != 1 or menu !=2:
    match menu:
            case "1":
                import random
                numero = random.randint(1,4)
                nombre = input("Introduce el nombre del alumno: ")
                casa1= "Gryffindor"
                casa2= "Slytherin"
                casa3= "Hufflepuff"
                casa4= "Ravenclaw"
                if numero == 1:
                    numero = str(numero) + " "+casa1
                elif numero == 2:
                    numero = str(numero) + " "+casa2
                elif numero == 3:
                    numero = str(numero) + " "+casa3
                elif numero == 4:
                    numero = str(numero) + " "+casa4
                    
                print("El sombrero dice que",nombre,"pertenece a",numero)
                
            case "2":
                print("Ejecutando y mostrando estadísticas")
            case _:
                print("Opción incorrceta")
        
    print("=========================")
    print("SOMBRERO SELECCIONADOR")
    print("=========================")
    print("Pulsa [1] para seleccionar casa para un alumno")
    print("Pulsa [2] para mostar estadísticas")
    menu = input("Introduce un número del menú y pusla enter...")
                                
