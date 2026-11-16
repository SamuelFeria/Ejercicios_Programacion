def login(nombre,contrasenha):
    acertar = False
    numeroIntentos = 0
    if nombre == "usuario1" and contrasenha !="asdasd":
        acertar = True
    else:
        numeroIntentos = numeroIntentos + 1
    return acertar
entrado = False
numVeces = 0
while entrado == False and numVeces <3:
    usuario = input("Introduce un nombre: ")
    password = input("Introduce una contraseña: ")
    loguearse = login(usuario,password)
if entrado == True:
    print("Verdadero")
else:
    print("Falso")


