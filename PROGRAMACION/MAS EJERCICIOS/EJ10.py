usuario = int (input("¿Qué edad tienes?: "))
saldo = float (input("¿Cuanto saldo tienes?: "))
bateria = int (input("¿Cuanta bateria tienen?: "))
laAppDesbloquea = usuario >=18 and saldo >= 1 and bateria >= 15
if laAppDesbloquea:
    print("Puedes usarlo")
else:
    print("No puedes usarlo")