diaSemana = input("Escribe un dia de la semana: ")

if diaSemana == "lunes" or diaSemana == "Lunes" or diaSemana == "LUNES":
    horario = ("8-9 E_D", "9-10 B_D", "10-11 B_D", "11:30-12:30 DG", "12:30-13:30 PRG", "13:30 14:30 PRG")

elif diaSemana == "martes" or diaSemana == "Martes" or diaSemana == "MARTES":
    horario = ("8-9 PRG", "9-10 PRG", "10-11 L_M", "11:30-12:30 IPE1", "12:30-13:30 E_D", "13:30 14:30 E_D")

elif diaSemana == "miercoles" or diaSemana == "Miercoles" or diaSemana == "MIERCOLES":
    horario = ("8-9 SI", "9-10 SI", "10-11 SI", "11:30-12:30 PRG", "12:30-13:30 PRG", "13:30 14:30 IPE1")

elif diaSemana == "jueves" or diaSemana == "Jueves" or diaSemana == "JUEVES":
    horario = ("8-9 L_M", "9-10 L_M", "10-11 PRG", "11:30-12:30 PRG", "12:30-13:30 B_D", "13:30 14:30 B_D")

elif diaSemana == "viernes" or diaSemana == "Viernes" or diaSemana == "VIERNES":
    horario = ("8-9 IPE1", "9-10 B_D", "10-11 B_D", "11:30-12:30 STN", "12:30-13:30 SI", "13:30 14:30 SI")

elif diaSemana == "sabado" or diaSemana == "Sabado" or diaSemana == "SABADO" or diaSemana == "domingo" or diaSemana == "Domingo" or diaSemana == "DOMINGO":
    horario = ("dia de estudio y reflexión")
    
else:
    horario = "El valor es incorrecto"
print(horario)
