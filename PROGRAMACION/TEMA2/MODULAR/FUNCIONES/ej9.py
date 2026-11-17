def login(nombre,contrasenha,numeroIntentos):
    acertar = False
    #numeroIntentos = 0
    if numeroIntentos <3:
        
        if nombre == "usuario1" and contrasenha =="asdasd":
            acertar = True
        else:
            numeroIntentos = numeroIntentos + 1
    return [acertar,numeroIntentos]

entrado = False
numVeces = 0
while entrado == False and numVeces <3:
    usuario = input("Introduce un nombre: ")
    password = input("Introduce una contraseña: ")
    loguearse = login(usuario,password,numVeces)
    numVeces = loguearse[1]
    entrado = loguearse[0]
    
if entrado:
    print("Verdadero",numVeces)
else:
    print("Falso",numVeces)


