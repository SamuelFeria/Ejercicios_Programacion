rareza = input("Introduce la rareza del brawler: 'C'(Común) 'R'(Rara) 'E'(Épico) 'L'(Legendario)").upper()
nombre = "Juan"
while rareza != "SALIR":
    match rareza:
        case "C":
            print("Elegiste rareza común")
            rareza = "Común"
            numero_trofeos = int(input("Introduce tus trofeos: "))
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