#El usuario introduce, en este orden: 6, 2, 9, 4, 0. Haced la traza y describid con una frase para qué sirve el programa.

num = int(input("Número: "))
mayor = num
cont = 0
while num != 0:
    if num > mayor:
        mayor = num
    cont = cont + 1
    num = int(input("Número: "))
print(mayor, cont)