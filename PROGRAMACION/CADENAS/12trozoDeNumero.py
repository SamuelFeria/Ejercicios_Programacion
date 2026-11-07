#Toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente, validando que el rango es válido
num = input("Introduce un número: ")
inicial = int(input("Introduce una posición inicial: "))
final = int(input("Introduce una posición final: "))
while inicial < 0 or final >= len(num) or inicial > final :
    inicial = int(input("Introduce una posición inicial: "))
    final = int(input("Introduce una posición final: "))
print(num[inicial:final+1])