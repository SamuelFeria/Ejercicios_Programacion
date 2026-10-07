num = int (input("Escribe un numero de mes: "))
match num:
    case 1 | 2 | 3:
        estacion = "Invierno."
    case 4 | 5 | 6:
        estacion = "Primavera."
    case 7 | 8 | 9:
        estacion = "Verano."
    case 10 | 11 | 12:
        estacion = "Otoño."
    case _:
        estacion = "No es una estacion válida."

print (estacion)

       
