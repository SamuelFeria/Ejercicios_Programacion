def convertirEspaciado(texto,cadenaTexto):
    texto = input("Introduce una frase: ")
    cadenaTexto = texto.split()
    return(cadenaTexto)

texto = input("Introduce una frase: ")
cadenaTexto = texto.split()
dividir = convertirEspaciado(texto,cadenaTexto)
print(dividir)