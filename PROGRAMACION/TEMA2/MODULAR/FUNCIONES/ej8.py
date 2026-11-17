from math import pi

def calcularArea(radio):
    area = radio**2*pi
    return area
def CalcularPerimetro(radio):
    perimetro = 2*pi*radio
    return perimetro
def calculaAreaYPerimetro(radio):
    area = calcularArea(radio)
    perimetro = CalcularPerimetro(radio)
    return [perimetro,area]

radioEntrada = int(input("Dame el radio de la circunferencia: "))
resultadoPerArea = calculaAreaYPerimetro(radioEntrada)
resultadoPerimetro = CalcularPerimetro(radioEntrada)
resultadoArea = calcularArea(radioEntrada)
print("El resultado del área y perímetro es:",resultadoPerArea)
print(resultadoPerArea[0],resultadoPerArea[1])    
