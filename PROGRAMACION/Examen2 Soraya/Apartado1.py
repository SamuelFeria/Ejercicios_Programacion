print("==== BRAW STARTS REGISTRO ====")
print("Elige [1] Guardar datos del brawler")
print("Elige [2] Registrar partida")
print("Elige [3] Mostrar resumen")
print("Elige [4] para terminar el programa")
menu = input("Elige una opcipon: ")
while menu != "4":
    match menu:
        case "1":
            print("Guardando los datos del brawler")
            
        case "2":
            print("Registrando")
            
        case "3":
            print("Resumiendo")
        
        case _:
            print("Opción no válida")   

    print("==== BRAW STARTS REGISTRO ====")
    print("Elige [1] Guardar datos del brawler")
    print("Elige [2] Registrar partida")
    print("Elige [3] Mostrar resumen")
    print("Elige [4] para terminar el programa")
    menu = input("Elige una opcipon: ")
print("Fin del programa")