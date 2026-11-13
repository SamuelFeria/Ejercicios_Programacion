print("=========================")
print("SOMBRERO SELECCIONADOR")
print("=========================")
print("Pulsa [1] para seleccionar casa para un alumno")
print("Pulsa [2] para mostar estadísticas")
menu = input("Introduce un número del menú y pusla enter...")
while menu != 1 or menu !=2:
    match menu:
            case "1":
                print("Ejecutando y seleccionando casa")
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
                                
