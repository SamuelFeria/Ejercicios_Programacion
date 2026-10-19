diaSemana=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print(diaSemana[6])
import random
lista=[]
for i in range(5) :
    numeroRandom=random.randint(0,8)
    lista.append(numeroRandom)
print(lista)
diaSemana.append("martes")
diaSemana.append("miercoles") 
diaSemana.append("jueves")  
print(diaSemana)
#multiplosTres=[0,3,6,9,12,15,18,....,60]
numero = 0
multiplosTres=[]
for i in range(20):
    multiplosTres.append(numero)
    numero+=3
print(multiplosTres)
print(len(multiplosTres))


