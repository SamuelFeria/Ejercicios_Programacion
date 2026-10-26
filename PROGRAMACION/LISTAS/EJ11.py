lista = []

for i in range(15):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

numero = int(input("Introduce numero: "))

while numero < 0 or numero >= len(lista):
    numero = int(input("El numero debe ser menor que 15. Introduce otro numero: "))

for vuelta in range(numero):
    ultimo = lista[-1]
    
    for i in range (len(lista)-1, 0, -1):
        lista[i] = lista[i - 1]
    lista[0] = ultimo

print(lista)