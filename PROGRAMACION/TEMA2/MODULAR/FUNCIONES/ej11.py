def mostrarMenu():
    print("====Menú====")
    print("Pulsa [1] si quieres pasar a minutos")
    print("Pulsa [2] si quieres pasar a horas")
    print("Pulsa [3] si quieres pasar a segundos")
    print("Pulsa [-1] si quieres salir del programa")
    opcion = input("Introduce la opción del menú que deseas ejecutar: ")
    while opcion != "-1":
        print("Opcion Incorrecta, vuelva a introducir una opción")
        print("====Menú====")
        print("Pulsa [1] si quieres pasar a minutos")
        print("Pulsa [2] si quieres pasar a horas")
        print("Pulsa [3] si quieres pasar a segundos")
        print("Pulsa [-1] si quieres salir del programa")
        opcion = input("Introduce la opción del menú que deseas ejecutar: ")

menu = mostrarMenu()