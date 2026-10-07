diaSemana = input("Escribe un dia de la semana: ")

match diaSemana :
    case "lunes" | "Lunes" | "LUNES":
        horario = "8-9 E_D", "9-10 B_D", "10-11 B_D", "11:30-12:30 DG", "12:30-13:30 PRG", "13:30 14:30 PRG"

    case "martes" | "Martes" | "MARTES":
        horario = "8-9 PRG", "9-10 PRG", "10-11 L_M", "11:30-12:30 IPE1", "12:30-13:30 E_D", "13:30 14:30 E_D"

    case "miercoles" |"Miercoles" | "MIERCOLES":
        horario = "8-9 SI", "9-10 SI", "10-11 SI", "11:30-12:30 PRG", "12:30-13:30 PRG", "13:30 14:30 IPE1"

    case "jueves" | "Jueves" | "JUEVES":
        horario = "8-9 L_M", "9-10 L_M", "10-11 PRG", "11:30-12:30 PRG", "12:30-13:30 B_D", "13:30 14:30 B_D"

    case "viernes"| "Viernes" | "VIERNES":
        horario = "8-9 IPE1", "9-10 B_D", "10-11 B_D", "11:30-12:30 STN", "12:30-13:30 SI", "13:30 14:30 SI"

    case "sabado" |"Sabado" | "SABADO" | "domingo" | "Domingo" | "DOMINGO" :
        horario = "dia de estudio y reflexión"

    case _:
        horario = "El valor es incorrecto"

print(horario)  