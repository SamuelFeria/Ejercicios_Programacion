numero = input("Introduce un número: ")
punto = "."
mil = ""
for i in range(len(numero)-1,-1,-3):
    mil = numero[i] + punto + numero
print(mil)
