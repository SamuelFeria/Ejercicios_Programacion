cadena = input("Introduce una frase: ")
subcadena= input("Introduce un caracter: ")
i = len(cadena)
es_igual = False
while subcadena[i] == cadena[i] and i > 0:
    if subcadena[i] == len(cadena[i]):
        es_igual = True
    i = i-1 
print(es_igual)
       