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
        
