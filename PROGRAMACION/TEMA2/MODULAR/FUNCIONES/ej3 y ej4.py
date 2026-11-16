def CalculaTemperaturaMedia(tempMax,tempMin,tempMedia):
    tempMedia = (tempMax + tempMin) / 2
    return tempMedia
numDias = int(input("Introduce el nº de días: "))
i = 0
tempMedia = 0
while i < numDias:
    tempMax = int(input("Introduce la temperatura máxima: "))
    tempMin = int(input("Introduce una temperatura mínima: "))
    mediaDia = CalculaTemperaturaMedia(tempMax,tempMin,tempMedia)
    i=i+1
    print(i)
    print(mediaDia)
        
    """
    def calculaMedia(min,max):
        media=(min+max)/2
        return media
    def pideYCalculaMedia():
        minE = int(inptu("Introduce temp minima: "))
        maxE = int(inptu("Introduce temp maxima: "))
        while minE > maxE:
            print("el minimo no puede ser mayor")
            maxE = int(inptu("Introduce temp maxima: "))
        resultado = calculaMedia(minE,maxE)
        return resultado
    
numVeces = int(input("Introduce numero de veces: "))
for i in range(numVeces):
    res = pideYCalculaMedia()
    print(res)
    """
