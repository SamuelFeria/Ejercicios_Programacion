def contarA(lista):
    lista_dentro = lista_fuera
    subcadena = lista_dentro[0]+lista_dentro[1]+lista_dentro[2]
    contador = 0
    for i in range (len(subcadena)):
        if subcadena[i] == "a":
          contador = contador + 1  
    return contador

lista_fuera = []
nombre = input("Introduce un nombre: ").lower()
lista_fuera.append(nombre)
apellido1 = input("Introduce tu primer apellido: ").lower()
lista_fuera.append(apellido1)
apellido2 = input("Introduce tu segundo apellido: ").lower()
lista_fuera.append(apellido2)

numero_letras = contarA(lista_fuera)
print("Tiene: "+str(numero_letras)+" a")

