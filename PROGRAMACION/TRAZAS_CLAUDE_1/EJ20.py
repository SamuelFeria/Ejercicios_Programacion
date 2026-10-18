#El usuario introduce, en este orden: 4, 6, 2, 1, 5. Además de la salida, decidme qué valores se consumen y cuáles no se llegan a leer.

n = int(input("Número: "))
suma = 0
i = 1
while i <= n:
    suma = suma + i
    i = i + 1
    n = int(input("Número: "))
print("Suma:", suma)