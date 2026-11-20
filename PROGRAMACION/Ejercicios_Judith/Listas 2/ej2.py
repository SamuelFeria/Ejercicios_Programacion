#Contar letras “a” (cadenas): pide una palabra por teclado y muestra cuántas veces aparece la letra a.
palabra = input("Introduce una palabra: ").lower()
contador = 0
for i in range (len(palabra)):
    if palabra[i] == "a":
        contador = contador +1
print("Hay:",contador,"Aes")