#Sin repetidos: pide palabras al usuario hasta que escriba "fin" y muestra una lista final que contenga cada palabra una sola vez, en el orden en que aparecieron por primera vez.
palabra = ""
lista_palabras = []
encontrado = False
while palabra != "fin":
    palabra = input("Escribe una palabra: ").lower()
    while encontrado == False and len(lista_palabras)>0:
        if palabra in lista_palabras:
            encontrado = True
        else:
            lista_palabras.append(palabra)
    
print(lista_palabras)
