#Vocales. Pide una palabra (solo letras minúsculas, sin tildes ni espacios). Escribe Vocales: con cuántas vocales tiene y, en otra línea, Otras: con cuántas letras no son vocales.
palabra = input("Introduce una palabra: ").lower()
letras = 0
contador = 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador = contador +1
    else:
        letras = letras +1
print("Tiene:",contador,"vocales y tiene:",letras,"consonantes")