num = int (input("Escribe un numero: "))

match num:
    case 0:
        mensajeCase = "CERO"
    case 1:
        mensajeCase = "UNO"
    case 2:
        mensajeCase = "DOS"
    case _:   
       mensajeCase = "OTROS"
print (mensajeCase)