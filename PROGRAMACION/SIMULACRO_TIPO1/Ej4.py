#Introduce el nombre del alumno
alumno = (input("Introduce el nombre del alumno: "))
#Introduce una nota entre (0-100)
nota = int(input("Introduce la nota del alumno (rango válido de 0 a 100): "))
#Si introduces un valor fuera de ese rango vuleve a pedir nota
if nota < 0 or nota > 100:
    nota = int(input("Vuelve a introducir una nota: "))
#Si el valor es correcto nos informe de las calificaciones:
#90-100 Sobresaliente
#70-89 Notable
#60-69 Bien
#50-59 Suficiente
#0-49 Suspenso
if nota < 101 and nota > 89:
    print("Sobresaliente")
if nota < 90 and nota > 69:
    print("Notable")
if nota < 70 and nota > 59:
    print("Bien")
if nota < 60 and nota > 49:
    print("Suficiente")
if nota < 50 and nota > 0 :
    print("Suspenso")
#El programa debe de repetir todo hasta que se escriba exit en el nombre del alumno
while alumno != "exit":
    alumno = (input("Introduce el nombre del alumno: "))
    nota = int(input("Introduce la nota del alumno (rango válido de 0 a 100): ")) 



