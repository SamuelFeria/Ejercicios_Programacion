opciones = int (input(" Elige 1 para mostrar litado de habitaciones o 2 si quieres ver el detalle de la habitacion: "))
listadoHabitaciones = ("1 Azul", "2 Roja", "3 Verde", "4 Rosa", "5 Gris")

match opciones:
    case 1:
        mensaje = listadoHabitaciones
    case 2:
        numeroHabitacion = int(input("Escribe el numero de habitaicon que queires ver: "))
        match numeroHabitacion:
            case 1:
                 mensaje = "La primera habitación es Azul tiene 2 camas y está en la primera planta."
            case 2:
                mensaje = "La segunda habitación es Roja tiene 1 cama y está en la primera planta."
            case 3: 
                mensaje = "La tercera habitación es Verde tiene 3 camas y está en la segunda planta."
            case 4:  
                mensaje = "La cuarta habitación es Rosa tiene 2 camas y está en la segunda planta."
            case 5:  
                mensaje =  "La quita habitación es Gris tiene 1 cama y está en la tercera planta."
            case _:
                mensaje = " No has elegido un nº de habitación válido."
print(mensaje)
        
            

        


