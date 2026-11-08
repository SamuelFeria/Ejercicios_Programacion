#Calificaciones. Pide cuántos alumnos hay (tiene que ser mayor que 0; si no, escribe Número no válido y lo vuelve a pedir). Después pide la nota de cada alumno (entre 0 y 10, ambas incluidas; si no, escribe Nota no válida y la vuelve a pedir). Al final escribe Aprobados: con cuántos tienen 5 o más y Media: con la media de las notas.
alumnos= int(input("Introduce el nº de alumnos: "))
while alumnos < 0:
    print("Número no válido")
    alumnos= int(input("Vuleve a introducir el nº de alumnos: "))
nota_alumnos=[]
for i in range(alumnos):
    nota_alumno = int(input("Introduce la nota del alumno: "))
    nota_alumnos.append(nota_alumno)
    while nota_alumno <0 or nota_alumno>10:
        print("Nota no válida")
        nota_alumno = int(input("Introduce la nota del alumno: "))
    aprobados = 0
for i in range (len(nota_alumnos)):
    if nota_alumnos[i] >=5:
        aprobados = aprobados +1 
    i = i+1
        
media = 0
for i in range (len(nota_alumnos)):
    media = media + nota_alumnos[i] / len(nota_alumnos)      
print("Alumnos aprobados:",aprobados,"y la media es:",media)

        
    
