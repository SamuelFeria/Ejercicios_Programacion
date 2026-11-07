#Pide números positivos hasta que se escriba 0 (el 0 no cuenta) y guárdalos en una lista. Escribe cuántos hay y su media. Si no hay ninguno, la media es 0.
lista=[]
num = 1
media = 0
suma = 0
while num !=0:
    num = int(input("Introduce un número: "))
    if num !=0:
        lista.append(num)
        suma = suma + num
if len(lista) > 0: 
    media = suma / len(lista)
print("Hay: ",len(lista),"números","y la media es:",media)