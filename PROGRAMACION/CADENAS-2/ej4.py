cadena = input("Introduce una frase: ").upper()
subcadena= input("Introduce un caracter: ").upper()
#print(cadena[:len(subcadena)] == subcadena)
i = 0
es_igual = False
while len(subcadena) <= len(cadena) and i < len(subcadena):
    if cadena[i] == subcadena[i]:
        comienza = True
    i = i + 1
print(es_igual)