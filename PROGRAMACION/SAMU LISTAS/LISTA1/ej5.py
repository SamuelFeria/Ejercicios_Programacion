#Sin repetidos: pide palabras al usuario hasta que escriba "fin" y muestra una lista final que contenga cada palabra una sola vez, en el orden en que aparecieron por primera vez.
palabra = ""
lista_palabras = []
encontrado = False
i = 0
while palabra != "fin":
    palabra = input("Escribe una palabra: ").lower()
    while encontrado == False and i < len(lista_palabras):
        if palabra in lista_palabras:
            encontrado = True
        else:
            lista_palabras.append(palabra)
            i = i + 1
    
print(lista_palabras)
