
print("=========================")
print("SOMBRERO SELECCIONADOR")
print("=========================")
print("Pulsa [1] para seleccionar casa para un alumno")
print("Pulsa [2] para mostar estadísticas")
menu = input("Introduce un número del menú y pusla enter...")
while menu != "1" or menu !="2" and nombre !="voldemort":
    match menu:
            case "1":
                import random
                numero = random.randint(1,4)
                nombre = input("Introduce el nombre del alumno: ").lower()
                casa1= "Gryffindor"
                casa2= "Slytherin"
                casa3= "Hufflepuff"
                casa4= "Ravenclaw"
                total_alumnos=0
                if numero == 1:
                    numero = str(numero) + " "+casa1
                    total_alumnos = total_alumnos +1
                elif numero == 2:
                    numero = str(numero) + " "+casa2
                    total_alumnos = total_alumnos +1
                elif numero == 3:
                    numero = str(numero) + " "+casa3
                    total_alumnos = total_alumnos +1
                elif numero == 4:
                    numero = str(numero) + " "+casa4
                    total_alumnos = total_alumnos +1
                print("El sombrero dice que",nombre,"pertenece a",numero)
                if nombre == "voldemort":
                    print("Aparittion, traspórtame a otro sitio")
                
            case "2":
                if total_alumnos == 0:
                    print("No hay alumnos")
                elif total_alumnos < 0:
                    print("Total de alumnos:",total_alumnos)
                    print(casa1,":",)
            
            case _:
                print("Opción incorrceta")
                
    print("=========================")
    print("SOMBRERO SELECCIONADOR")
    print("=========================")
    print("Pulsa [1] para seleccionar casa para un alumno")
    print("Pulsa [2] para mostar estadísticas")
    menu = input("Introduce un número del menú y pusla enter...")
                                
