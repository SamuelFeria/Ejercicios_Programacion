def calcularHoras (tiempo):
    cantidad = tiempo//3600
    hora = cantidad
    return hora

def calcularMinutos(tiempo):
    cantidad = tiempo//60
    minutos = cantidad
    return minutos

def horasYMinutos():
    segundos = int(input("Introduce los segundos: "))
    horas = calcularHoras()
    minutos = calcularMinutos()
    return [horas,minutos]

print(segundos,"segundos serán: ",horas,minutos,)
