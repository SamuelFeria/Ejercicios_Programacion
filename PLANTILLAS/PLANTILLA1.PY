# =====================================================================
# PLANTILLA UNIVERSAL DE EXAMEN (menú + listas + estadísticas)
# Estilo "paso a paso": un bucle por cada cálculo, una variable por dato.
# Sustituye los textos [ENTRE CORCHETES] por los del enunciado.
# =====================================================================

# ---------------------------------------------------------------------
# 0. CHECKLIST ANTES DE ENTREGAR
# ---------------------------------------------------------------------
# [ ] Los textos coinciden LETRA POR LETRA con el enunciado
#     (mayúsculas, tildes, dos puntos, plurales, espacios).
# [ ] No queda ningún print de depuración (print(lista), etc.).
# [ ] Caso "no hay datos" controlado en listado y estadísticas.
# [ ] Acumuladores (suma, contador) inicializados ANTES del bucle.
# [ ] Bucles de búsqueda con while: i = 0 justo antes.
# [ ] Valores de lista[0] solo se leen dentro del if len(lista) > 0.
# [ ] Valores centinela (999, "salir") no se procesan como datos.
# [ ] Lo que el enunciado pide "una por línea" va en prints separados.
# [ ] Probado con: sin datos, 1 dato, varios datos, empates, valores
#     en los límites (0, 10, 5, -50, 60...).


# ---------------------------------------------------------------------
# 1. ESQUELETO DEL MENÚ (se repite hasta escribir "salir")
#    Patrón: mostrar menú -> leer -> while != "salir" -> match
#    -> al final del bucle volver a mostrar y leer.
#    Así "salir" nunca entra en el match y no hace falta "pass".
# ---------------------------------------------------------------------
lista_nombres = []       # lista 1 (ej: títulos)
lista_valores = []       # lista 2 (ej: valoraciones)

print("==============================")
print("[TÍTULO DEL MENÚ]")
print("==============================")
print("   1. [Añadir]")
print("   2. [Mostrar listado]")
print("   3. [Mostrar estadísticas]")
menu = input('Elige una opción. Para salir, escribe "salir". ')

while menu != "salir":
    match menu:
        case "1":
            # ---- ver bloque 2 (pedir y validar) ----
            nombre = input("[Introduce el nombre]: ")
            while nombre == "":
                print("[Nombre no válido]")
                nombre = input("[Introduce el nombre]: ")

            valor = float(input("[Introduce el valor]: "))
            while valor < 0 or valor > 10:
                print("[Valor no válido]")
                valor = float(input("[Introduce el valor]: "))

            # Se guarda DESPUÉS de validar los dos
            lista_nombres.append(nombre)
            lista_valores.append(valor)
            print("[Serie añadida]")

        case "2":
            # ---- ver bloque 3 (listado) ----
            if len(lista_nombres) == 0:
                print("[No hay series]")
            else:
                for i in range(len(lista_nombres)):
                    print("   " + str(i + 1) + ". " + lista_nombres[i] + ": " + str(lista_valores[i]))

        case "3":
            # ---- ver bloque 4 (estadísticas) ----
            if len(lista_nombres) == 0:
                print("[No hay series]")
            else:
                # TOTAL
                total = 0
                for i in range(len(lista_nombres)):
                    total = total + 1
                print("Total: ", total)

                # MEDIA
                suma = 0
                for i in range(len(lista_valores)):
                    suma = suma + lista_valores[i]
                media = suma / len(lista_valores)
                print("Media:", media)

                # MEJOR (máximo) con su posición; en empate se queda la primera
                mejor = lista_valores[0]
                pos_mejor = 0
                for i in range(len(lista_valores)):
                    if lista_valores[i] > mejor:      # > (no >=) = gana la primera
                        mejor = lista_valores[i]
                        pos_mejor = i
                print("Mejor:", lista_nombres[pos_mejor], "(posición", pos_mejor + 1, ")")

                # PEOR (mínimo): igual pero con <
                peor = lista_valores[0]
                pos_peor = 0
                for i in range(len(lista_valores)):
                    if lista_valores[i] < peor:
                        peor = lista_valores[i]
                        pos_peor = i

                # CONTAR los que cumplen una condición
                cuantos = 0
                for i in range(len(lista_valores)):
                    if lista_valores[i] >= 8:
                        cuantos = cuantos + 1
                print("Recomendadas:", cuantos)

                # CONTAR textos que empiezan por algo (exacto, con mayúscula)
                con_the = 0
                for i in range(len(lista_nombres)):
                    if lista_nombres[i][0:3] == "The":
                        con_the = con_the + 1
                print("Empiezan por The:", con_the)

                # BUSCAR EL PRIMERO que cumple y parar (while + bandera)
                i = 0                                  # <- IMPRESCINDIBLE
                encontrada = False
                while i < len(lista_valores) and encontrada == False:
                    if lista_valores[i] < 5:
                        encontrada = True
                    else:
                        i = i + 1
                if encontrada:
                    print("Primera floja:", lista_nombres[i])
                else:
                    print("Primera floja: ninguna")

        case _:
            print("Opción incorrecta")

    # Volver a mostrar el menú y leer (mismo texto que arriba)
    print("==============================")
    print("[TÍTULO DEL MENÚ]")
    print("==============================")
    print("   1. [Añadir]")
    print("   2. [Mostrar listado]")
    print("   3. [Mostrar estadísticas]")
    menu = input('Elige una opción. Para salir, escribe "salir". ')

print("Hasta la próxima")


# =====================================================================
# PATRONES SUELTOS (copiar y adaptar)
# =====================================================================

# ---- A. Pedir y validar un entero > 0 -------------------------------
# n = int(input("Introduce un número: "))
# while n <= 0:
#     print("Número no válido")
#     n = int(input("Introduce un número: "))

# ---- B. Texto no vacío (sin strip) ----------------------------------
# texto = input("Introduce un texto: ")
# while texto == "":
#     print("Texto vacío")
#     texto = input("Introduce un texto: ")
# (Si debe rechazar también solo espacios: palabras = texto.split()
#  y repetir mientras len(palabras) == 0.)

# ---- C. Valor CENTINELA (ej: 999 termina) ---------------------------
# Leer ANTES del bucle y al FINAL de cada vuelta, así el 999 no se procesa.
# x = int(input("Introduce un número: "))
# contador = 0
# suma = 0
# while x != 999:
#     if x >= -50 and x <= 60:          # solo las válidas cuentan
#         suma = suma + x
#         contador = contador + 1
#     else:
#         print("Temperatura no válida")
#     x = int(input("Introduce un número: "))
# if contador == 0:
#     print("No hay temperaturas")
# else:
#     print("Media:", suma / contador)

# ---- D. Máximo / mínimo sin lista (primer dato válido fija ambos) ---
# if contador == 0:
#     maxima = x
#     minima = x
# else:
#     if x > maxima:
#         maxima = x
#     if x < minima:
#         minima = x

# ---- E. Tramos con if / elif (de menor a mayor) ---------------------
# if peso <= 1:
#     precio = 5
# elif peso <= 5:        # aquí ya sabe que peso > 1
#     precio = 8
# else:
#     precio = 12
# if urgente == "s":
#     precio = precio + 3

# ---- F. Contar letras (vocales / otras) -----------------------------
# vocales = 0
# otras = 0
# for letra in palabra:
#     if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#         vocales = vocales + 1
#     else:
#         otras = otras + 1

# ---- G. Repetir hasta que ocurra algo (dados) -----------------------
# import random
# suma = 0
# lanzamientos = 0
# while suma != 7:
#     d1 = random.randint(1, 6)
#     d2 = random.randint(1, 6)
#     suma = d1 + d2
#     lanzamientos = lanzamientos + 1
#     print("Dados:", d1, "y", d2)

# ---- H. Palabra más larga (en empate, la primera) -------------------
# palabras = texto.split()
# larga = palabras[0]
# for palabra in palabras:
#     if len(palabra) > len(larga):     # > estricto
#         larga = palabra

# =====================================================================
# ERRORES MÁS COMUNES (los que quitan puntos)
# =====================================================================
# 1. Textos distintos al enunciado ("Minima" vs "Mínima:").
# 2. Procesar el valor centinela (999) como si fuera un dato.
# 3. lista[0] fuera del if que comprueba que hay datos -> IndexError.
# 4. Olvidar i = 0 antes de un while de búsqueda.
# 5. Dividir entre len(lista) o contador sin comprobar que no es 0.
# 6. Guardar un dato antes de validarlo.
# 7. Comparar con "the" cuando el enunciado dice "The".
# 8. Mezclar and/or sin paréntesis.
# 9. Mensajes de más (print("válida")) que el enunciado no pide.
# 10. Inicializar suma/contador DENTRO del bucle (se reinician).