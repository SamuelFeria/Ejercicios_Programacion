humano = int(input("Introduce un nº entre 0 y 5: "))
maquina = int(input("Introduce un nº entre 0 y 5: "))
suma = humano + maquina
resultado = input("Introduce par o impar: ").lower()
if resultado == "par" and suma %2==0:
    print("Gana: humano")
elif resultado == "impar" and suma %2==1:
    print("Gana: humano")
elif resultado == "par" and suma %2==1:
    print("Gana: maquina")  
elif resultado == "impar" and suma %2==0:
    print("Gana: maquina") 
