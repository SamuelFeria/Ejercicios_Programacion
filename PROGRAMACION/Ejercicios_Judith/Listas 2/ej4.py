#Iniciales (cadenas): pide el nombre completo de un personaje (nombre y apellidos separados por espacios) y muestra sus iniciales en mayúscula separadas por puntos.
nombre_completo = input("Introduce nombre, espacio apellido1  espacio apellido2: ").upper()
subcadena = nombre_completo.split()
iniciales = ""
palabra = subcadena[0]

for i in range (len(subcadena)):
    palabra = subcadena[i]
    iniciales = iniciales + palabra[0]+"."

print(iniciales)
