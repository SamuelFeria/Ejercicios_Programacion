cuota = input (" ¿Está pagada la cuota?, ¿Si o No?: ")
horario = float (input (" ¿Que hora es?: "))
plazaReservada = int (input (" ¿que n1 de plaza reservaste?: "))
if cuota == "Si" and horario >= 7.00 and horario < 22.00 and plazaReservada > 0 and plazaReservada < 26:

    print (" Tienes la cuota pagada, esta abierto y la plaza fue reservada ")
    
else: 
    print ("fin.") 