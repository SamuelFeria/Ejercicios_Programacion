lista=['elefante','perro','gato']
animal= input("Introduce un animal: ")
encontrado = False
posicion = 0
while not encontrado and posicion < len(lista):
    if lista[posicion]== animal:
        encontrado = True
    else:
        posicion = posicion+ 1
if encontrado:
    print("El animal se encuentra en la posicion: ", posicion)
else:
    print("El" , animal ,"no se añade a la lista")


