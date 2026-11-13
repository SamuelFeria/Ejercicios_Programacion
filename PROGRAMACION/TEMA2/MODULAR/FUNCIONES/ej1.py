def obtieneYValidaDatosDeEntrada ():
    num = int(input("introduce un número positivo: "))
    while num < 0 :
        num = int(input("introduce un número positivo: "))
    return num

numero = obtieneYValidaDatosDeEntrada()
print(numero)
