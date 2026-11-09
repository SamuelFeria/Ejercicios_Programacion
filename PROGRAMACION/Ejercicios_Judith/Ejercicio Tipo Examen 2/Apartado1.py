print("==============")
print("MI CATÁLOGO DE SERIES")
print("==============")
print("Elige [1] para añadir serie")
print("Elige [2] para mostrar el listado de tus series ")
print("Elige [3] para mostar estadísticas")
menu = input("Elige una opción. Para salir, escirbe 'salir'... ").lower()
while menu != "salir":
    match menu:
        case "1":
            print("Ejecutando añadir")
        case "2":
            print("Ejecutando listado")
        case "3":
            print("Ejecutando estadísticas")
        case _:
            print("Opción incorrecta")
    print("==============")
    print("MI CATÁLOGO DE SERIES")
    print("==============")
    print("Elige [1] para añadir serie")
    print("Elige [2] para mostrar el listado de tus series ")
    print("Elige [3] para mostar estadísticas")
    menu = input("Elige una opción. Para salir, escirbe 'salir'... ")
print("Hasta la próxima")


