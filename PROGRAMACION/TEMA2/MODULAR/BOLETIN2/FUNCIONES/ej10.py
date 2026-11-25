def calcularHoras (tiempo):
    cantidad = tiempo//3600
    hora = cantidad
    return hora

def calcularMinutos(tiempo,hora):
    segundos_res = segundos- 3600 * hora
    contador = 0
    while segundos_res > 60:
        contador = contador +1
        segundos_res = segundos_res- 60
    minutos = contador
    return minutos

def clacularSegundos(horas,minutos):
    horas = calcularHoras()
    minutos = calcularMinutos()
    return [horas,minutos]
segundos = int(input("Introduce segundos: "))
horas = calcularHoras(segundos)
minutos = calcularMinutos(segundos,horas)
print(segundos,"segundos serán: ",horas,"horas",minutos,"minutos")
