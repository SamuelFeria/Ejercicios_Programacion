#¿Está en el plantel? (listas y búsqueda con while): dada la lista ["Mario", "Luigi", "Peach", "Bowser"], pide un nombre por teclado y muestra si está en la lista y en qué posición.
lista = ["Mario", "Luigi", "Peach", "Bowser"]
nombre = input("Introduce un nombre: ")
i = 0
encontrado = False
while i < len(lista) and encontrado == False:
    if lista[i] == nombre:
        encontrado = True
    else:
        i = i + 1
if encontrado:
    print("esta en la lista",i)
else:
    print("no esta")
