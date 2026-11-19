def mostrarMenu():
    print("====Menú====")
    print("Pulsa [1] si quieres pasar a minutos")
    print("Pulsa [2] si quieres pasar a horas")
    print("Pulsa [3] si quieres pasar a segundos")
    print("Pulsa [-1] si quieres salir del programa")
    opcion = input("Introduce la opción del menú que deseas ejecutar: ")
    while opcion != "-1":
        print("Opcion Incorrecta, vuelva a introducir una opción")
        print("====Menú====")
        print("Pulsa [1] si quieres pasar a minutos")
        print("Pulsa [2] si quieres pasar a horas")
        print("Pulsa [3] si quieres pasar a segundos")
        print("Pulsa [-1] si quieres salir del programa")
        opcion = input("Introduce la opción del menú que deseas ejecutar: ")
        
def calcularHoras (tiempo):
    cantidad = tiempo//3600
    hora = cantidad
    return hora

def calcularMinutos(tiempo,hora):
    segundos_res = segundos - 3600 * 1
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

menu = mostrarMenu()
segundos = int(input("Introduce segundos: "))
horas = calcularHoras(segundos)
minutos = calcularMinutos(segundos,horas)
print(segundos,"segundos serán: ",horas,"horas",minutos,"minutos")