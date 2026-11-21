#Lista invertida: crea una lista con varias palabras introducidas por el usuario y muestra la lista con los elementos en orden inverso, sin modificar la original.
lista_palabras = []
lista_inversa = []
inversa = ""
while len(lista_palabras) < 2:
    palabra = input("Introduce una palabra: ")
    lista_palabras.append(palabra)

for i in range(len(lista_palabras)-1,-1,-1):
   inversa = inversa + lista_palabras[i]
   lista_inversa.append(lista_palabras[i])

print(lista_inversa)