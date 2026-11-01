num= int(input("Introduce un número: "))
lista=[]
sumaNumeros=0
while num !=0: 
    lista.append(num)
    num = int(input("Introduce un número: "))
    sumaNumeros = sumaNumeros + num
if len(lista) >0:
    creciente = True
    decreciente = False
    for i in range(len(lista)-1):
        if lista[i] < lista[i+1]:
            decreciente = False
        if lista[i] > lista[i+1]:
            creciente = False
    if creciente:
        print("creciente")
    elif decreciente:
        print("decreciente")
    else:
        print("desordenado")
    print("Números introducidos (contando el 0): ", len(lista)+1)
    media= sumaNumeros / len(lista)
    print("La media es: ", media)
   