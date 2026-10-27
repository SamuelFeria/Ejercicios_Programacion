nombre = input("introduce un nombre: ")
pasword = "inicio1234"
while nombre != "usuario1":
    print("usuario incorrecto")
    nombre = input("introduce un nombre: ")
clave=input("introduce clave: ")
while clave != pasword:
    print("contraseña incorrecta")
    clave=input("introduce clave: ")       
print("Usuario logueado")


