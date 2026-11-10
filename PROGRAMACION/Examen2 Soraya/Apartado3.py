print("==== BRAW STARTS REGISTRO ====")
print("Elige [1] Guardar datos del brawler")
print("Elige [2] Registrar partida")
print("Elige [3] Mostrar resumen")
print("Elige [4] para terminar el programa")
menu = input("Elige una opcipon: ")
modo_de_juego = ""
partidas = 0
trofeos = 0
total_trofeos = ""
nombre =""
rareza=""
numero_trofeos = 0
while menu != "4":
    match menu:
        case "1":
            print("Guardando los datos del brawler")
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
            #modo de juego
            modo_de_juego = input("Introduce el modo de juego 'G'(Atrapagemas) 'B'(Balón Brawl) 'N'(Noqueo) 'S'(Supervivencia)").upper()
            while modo_de_juego != "G" or modo_de_juego != "B" or modo_de_juego != "N" or modo_de_juego != "S":
                modo_de_juego = input("Introduce el modo de juego 'G'(Atrapagemas) 'B'(Balón Brawl) 'N'(Noqueo) 'S'(Supervivencia)").upper()
            if modo_de_juego == "G" or modo_de_juego == "B" or modo_de_juego == "N":
                resultado = input("Introduce un resultado 'V'(Victoria) 'D'(Derrota) 'E'(Empate): ").lower()
            else:
                posicion = int(input("Introduce la posición posicion (1-10): "))
            
            #trofeos   
            if resultado == "Victoria":
                trofeos = trofeos + 10
                total_trofeos = trofeos
            if resultado == "Derrota":
                trofeos = trofeos - 5
                total_trofeos = trofeos
            if modo_de_juego == "S":
                if posicion == 1:
                    trofeos = trofeos + (12-2)
                    total_trofeos = trofeos
                if posicion == 2:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion == 3:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion == 4:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion == 5:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion == 6:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion == 7:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion == 8:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion == 9:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
                if posicion ==10:
                    trofeos = trofeos + (12-2*posicion)
                    total_trofeos = trofeos
            
            print("El brawler:","ha conseguido:",trofeos,"en esta partida","su total es",total_trofeos)
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