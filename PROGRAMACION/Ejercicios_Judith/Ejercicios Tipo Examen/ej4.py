#Palabras. Pide un texto (si está vacío, escribe Texto vacío y lo vuelve a pedir). Escribe Palabras: con cuántas palabras tiene y, en otra línea, Más larga: con la palabra más larga (si hay empate, la primera).
texto =input("Introduce un texto: ")

while texto == "":
    print("Texto vacío")
    texto = input("Introduce un texto: ")
palabras = texto.split()
palabra_larga = palabras[0]
for palabra in palabras:
    if len(palabra) > len(palabra_larga):
        palabra_larga = palabra

print("El texto contiene:",len(palabras),"palabras")
print("La palabra más larga es:",palabra_larga)


