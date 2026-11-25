def menu():
    print("====MENU===")
    print("Pulsa [a] si deseas consultar la media: ")
    print("Pulsa [b] si deseas saber los nº pares: ")
    print("Pulsa [c] si deseas saber los nº negativos: ")
    print("Pulsa [d] si deseas calcular la suma: ")
    menu = input("Introduce una letra para acceder al menu: ").lower()
    while menu == "fin":
        print("Opción incorrecta")
        print("=====================")
        print("====MENU===")
        print("Pulsa [a] si deseas consultar la media: ")
        print("Pulsa [b] si deseas saber los nº pares: ")
        print("Pulsa [c] si deseas saber los nº negativos: ")
        print("Pulsa [d] si deseas calcular la suma: ")
        menu = input("Introduce una letra para acceder al menu: ").lower()
    return menu