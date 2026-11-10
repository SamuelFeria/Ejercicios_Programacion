print("==== BRAW STARTS REGISTRO ====")
print("Elige [1] Guardar datos del brawler")
print("Elige [2] Registrar partida")
print("Elige [3] Mostrar resumen")
print("Elige [4] para terminar el programa")
menu = input("Elige una opcipon: ")
nombre =""
rareza=""
numero_trofeos = 0
partidas = 0
while menu != "4":
    match menu:
        case "1":
            print("Guardando los datos del brawler")
            nombre = input("Introduce el nombre del brawler: ")
            rareza = input("Introduce la rareza del brawler: 'C'(Común) 'R'(Rara) 'E'(Épico) 'L'(Legendario): ").upper()
            while rareza != "SALIR":
                match rareza:
                    case "C":
                        print("Elegiste rareza común")
                        rareza = "Común"
                        numero_trofeos = int(input("Introduce tus trofeos: "))
                        print("Registrandos los datos del brawler: ",nombre,rareza,numero_trofeos)
                    case "R":
                        print("Elegiste rareza rara")
                        rareza = "Rara"
                        numero_trofeos = int(input("Introduce tus trofeos: "))
                        print("Registrandos los datos del brawler: ",nombre,rareza,numero_trofeos)
                        
                    case "E":
                        print("Elegiste rareza épica")
                        rareza = "Épica"
                        numero_trofeos = int(input("Introduce tus trofeos: "))
                        print("Registrandos los datos del brawler: ",nombre,rareza,numero_trofeos)
                        
                    case "L":
                        print("Elegiste raraza legendaria")
                        rareza = "Legendaria"
                        numero_trofeos = int(input("Introduce tus trofeos: "))
                        print("Registrandos los datos del brawler: ",nombre,rareza,numero_trofeos)
                        
                    case _:
                        print("Opcion Incorrecta")
                rareza = input("Introduce la rareza del brawler: 'C'(Común) 'R'(Rara) 'E'(Épico) 'L'(Legendario)").upper()          
            print("Fin del programa")
                        

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