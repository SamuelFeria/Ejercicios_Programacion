num = int(input("Introduce un número: "))
exponente = int(input("Introduce un número: "))
resultado = 1
while num <0 or exponente <0:
    print("los dos numeros tienen que ser positivo")
    num = int(input("Introduce un número: "))
    exponente = int(input("Introduce un número: "))
for i in range (exponente):
    resultado = resultado * num
print(resultado)