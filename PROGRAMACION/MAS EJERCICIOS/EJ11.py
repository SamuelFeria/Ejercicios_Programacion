pulseraVip = input("¿Tienes pulsera VIP? ¿si o no?: ")
entradaEarlyBird = input("¿Tienes entrada early bird? ¿si o no?: ")
CanjePuntosApp = int (input("¿Cuantos puntos has canjeado en la APP?: "))
puedoEntrar = pulseraVip == "si" or (entradaEarlyBird == "si" and CanjePuntosApp >= 500)
if puedoEntrar:
    print("Puedo entrar en la zona VIP")
else:
    print("No puedo entrar en la zona VIP")
