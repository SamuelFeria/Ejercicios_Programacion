texto = "La inyección de SQL es un tipo de ciberataque encubierto en el cual un hacker inserta código propio en un sitio web con el fin de quebrantar las medidas de seguridad y acceder a datos protegidos. Una vez dentro, puede controlar la base de datos del sitio web y secuestrar la información de los usuarios. Le explicamos cómo funcionan los ataques de inyección de SQL, cómo combatirlos y cómo una herramienta antivirus potente lo puede proteger contra las consecuencias."
print("=======MENÚ=======")
print("Pulsa A si deseas ver las frases separadas")
print("Pulsa B si deseas saber cuantas frases hay")
print("Pulsa C si deseas saber cuantas palabras hay")
print("Pulsa D si deseas saber cuántas palabras tiene cada frase")
menu = input("Pulsa una tecla...").upper()
while menu != "9999":
    match menu:
        case "A":
            frases = texto.split(".")
            for frase in frases:
                if len(frase)>0:
                    print(frase+".")
        case "B":
            frases = texto.split(".")
            contador = 0
            for frase in frases:
                if len(frase)>0:
                    contador = contador + 1
            print("Hay:",contador)
        case "C":
            palabras = texto.split()
            print(len("Hay:",palabras))
        case "D":
            frases = texto.split(".")
            for frase in frases:
                if len(frase)>0:
                    palabras = frase.split()
                    print(len(palabras))
        case _:
            print("Opción no válida")

    print("=======MENÚ=======")
    print("Pulsa A si deseas ver las frases separadas")
    print("Pulsa B si deseas saber cuantas frases hay")
    print("Pulsa C si deseas saber cuantas palabras hay")
    print("Pulsa D si deseas saber cuántas palabras tiene cada frase")
    menu = input("Pulsa una tecla...")
print("Fin")

