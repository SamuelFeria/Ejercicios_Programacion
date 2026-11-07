cadena = input("Introduce una frase: ").upper()
subcadena= input("Introduce un caracter: ").upper()
es_igual = False
i = -1
inicio= len(cadena) - len(subcadena)
while len(subcadena) <= len(cadena) and i < len(subcadena):
    if cadena [inicio+1] == subcadena[i]:
        es_igual = True
    i = i + 1
print(es_igual)
       