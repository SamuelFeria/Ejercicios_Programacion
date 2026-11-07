nombre = input("Introduce un nombre: ")
apellido1 = input("Introduce el primer apellido: ")
apellido2 = input("Introduce el segundo apellido: ")
while len(nombre)<1 or len(apellido1)<1 or len(apellido2)<1:
    nombre = input("Introduce un nombre: ")
    apellido1 = input("Introduce el primer apellido: ")
    apellido2 = input("Introduce el segundo apellido: ")
print(apellido1[0].upper()+apellido1[1:]+" "+apellido2[0].upper()+apellido2[1:]+" "+nombre[0].upper()+nombre[1:])
print(apellido1[0].upper()+apellido1[1:-1]+apellido1[-1].upper()+" "+apellido2[0].upper()+apellido2[1:-1]+apellido2[-1].upper()+" "+nombre[0].upper()+nombre[1:-1]+nombre[-1].upper())