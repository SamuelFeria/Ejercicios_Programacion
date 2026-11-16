def convertirEspaciado(texto):
    textoEspacio= ""
    for i in range (len(texto)):
        if texto[i] != " ":
            textoEspacio= textoEspacio + texto[i] + " "
    return textoEspacio

texto = input("Introduce una frase: ")
print(convertirEspaciado(texto))