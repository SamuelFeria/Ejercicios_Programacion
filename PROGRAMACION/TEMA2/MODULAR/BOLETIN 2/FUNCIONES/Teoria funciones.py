La idea: programación modular (diapositivas 2 y 3)
Programación modular = dividir un problema grande en problemas pequeños, y resolver cada uno por separado en un trozo de código con nombre.
Hasta ahora escribías todo el programa seguido, de arriba abajo. Ahora lo troceamos en "cajitas" (así las llamó tu profesora en ej1.py). Cada cajita hace una sola cosa.
El ejemplo de la diapositiva 3: pedir una cadena de más de 4 caracteres, pedir un número y, según el número, enseñar unos caracteres. Se puede partir en dos cajitas:
• Cajita 1: leer y validar la cadena (que tenga más de 4 caracteres). Es el while de validación que ya conoces del Tema 1.
• Cajita 2: sacar una subcadena (calculaSubcadena). Se usa tres veces, solo cambian las posiciones.
Ventajas, en palabras sencillas:
• Escribes el código una vez y lo usas todas las veces que quieras.
• Si hay un fallo, lo arreglas en un solo sitio.
• El programa principal queda corto y se lee como una lista de pasos.
2. ¿Qué es una función? (diapositivas 4 y 5)
Una función es un bloque de código con nombre que escribes una vez (la defines) y puedes usar muchas veces (la llamas).
Piensa en una máquina de zumos: metes naranjas (lo que recibe), la máquina trabaja, y te da un zumo (lo que devuelve). No tienes que saber cómo funciona dentro cada vez que la usas.
Tres ideas de las diapositivas:
• Un grupo de funciones forma una librería (o módulo). Por eso en clase hiciste libreria.py.
• Para usar una librería se hace import, igual que import random o import math. Con import libreria usas libreria.esPar(num).
• Una función se puede llamar desde otros ficheros de Python. Eso es lo que haces con principal.py, que llama a lo que hay en libreria.py.
Las funciones que ya usabas sin saberlo: print(), input(), len(), int(), random.randint(). Alguien las escribió antes y tú solo las llamas.
3. Cómo se escribe: def (diapositiva 6)
La forma es siempre la misma:
def nombre(parametro1, parametro2):
    # cuerpo: lo que hace la función (con sangría)
    return valor
• def avisa a Python de que vas a crear una función.
• nombre lo eliges tú. Si dice qué hace, mejor: esPar, calculaArea.
• Los paréntesis llevan los parámetros: los datos que la función necesita para trabajar. Pueden ser ninguno, uno o varios, separados por comas.
• Los dos puntos : y la sangría (4 espacios) marcan qué línea es parte de la función, igual que en un if o un while.
• return es opcional (sección 4).
Ejemplo de la diapositiva:
def suma(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado
Importante: escribir el def no ejecuta nada. Solo guarda la receta. La función trabaja cuando la llamas (sección 5).
Cuando llamas a la función, el programa salta al def, ejecuta el cuerpo y termina al llegar al final o a un return. Después vuelve a la línea desde la que la llamaste.
4. return: lo que devuelve la función (diapositiva 7)
return es lo que la función te entrega cuando termina. Es como el zumo que sale de la máquina.
return y print NO son lo mismo (tú ya lo apuntaste en tu libreria.py, es lo más importante del tema):
• return entrega el valor a quien llamó a la función, y luego puedes guardarlo en una variable.
• print solo lo pinta en pantalla. Después no lo puedes usar: si lo guardas en una variable, esa variable vale None (nada).
Mira la diferencia:
def sumaConReturn(a, b):
    return a + b

def sumaConPrint(a, b):
    print(a + b)

x = sumaConReturn(2, 3)
print(x)    # sale 5

y = sumaConPrint(2, 3)   # aquí ya sale 5 por pantalla
print(y)    # sale None: la función no devolvió nada
Otras cosas de la diapositiva:
• return es opcional. Una función que solo muestra cosas (por ejemplo un menú) puede no tener.
• Puede haber varios return en una función, pero no queda bonito. Mejor uno solo al final, como en tu esPar: guardas el resultado en una variable y haces return resultado al final.
• Cuando Python llega a un return, la función termina ahí mismo.
Devolver varios valores: un return solo devuelve una cosa, así que metes los valores en una lista (o tupla).
def areaYPerimetro(radio):
    perimetro = 2 * 3.14 * radio
    area = 3.14 * radio * radio
    return [perimetro, area]

resultado = areaYPerimetro(2)
print(resultado[0])   # el perímetro
print(resultado[1])   # el área
5. Llamar a una función (diapositivas 8, 9 y 10)
Llamar = escribir su nombre con paréntesis y darle los datos. La llamada va fuera de la definición, en el programa principal.
def suma(numero_1, numero_2):
    return numero_1 + numero_2

print(suma(53, 2))      # sale 55
Formas de usar lo que devuelve:
res = suma(53, 2)       # guardarlo en una variable
print(res)

print(suma(53, 2))      # pintarlo directamente
• Si llamas a la función y no haces nada con lo que devuelve, el valor se pierde. Si quieres usarlo después, guárdalo en una variable.
• Los datos que escribes en la llamada (53 y 2) se llaman argumentos y se asignan a los parámetros por orden: numero_1 vale 53 y numero_2 vale 2.
• Funciona también con texto: suma("cadena ", "de texto") devuelve cadena de texto, porque + une textos.
Llamadas anidadas (diapositiva 10): una llamada puede ir dentro de otra. Python resuelve primero la de dentro.
print(suma(suma(53, 2), 3))   # suma(53,2) = 55, luego suma(55,3) = 58
Función de una librería, como en tu principal.py:
import libreria

num = int(input("Dame un número: "))
res = libreria.esPar(num)
print(res)
6. Argumentos por defecto (diapositiva 11)
Un parámetro puede traer un valor ya puesto. Si al llamar no das ese dato, se usa el valor por defecto.
def saludar(nombre = "Desconocido"):
    print("Hola " + nombre)

saludar()          # Hola Desconocido
saludar("Pepe")    # Hola Pepe
Se escribe con = dentro del paréntesis del def. Si das el dato en la llamada, gana el que das tú.
7. Cómo leer el enunciado de una función
En el boletín el enunciado te dice casi todo. Esta tabla traduce las frases típicas a código:
El enunciado dice
Lo escribes así
"no recibe ningún parámetro"
def nombre(): (paréntesis vacíos)
"recibe X e Y"
def nombre(x, y):
"devuelve" un número, texto, True/False
return valor
"muestra" o "imprime"
print(...) y no hace falta return
"devuelve el máximo y el mínimo"
return [maximo, minimo]
"programa principal que pide..."
código fuera de la función, abajo del todo
Ejemplo con el ejercicio 1 del boletín: "obtieneYValidaDatosDeEntrada: no recibe nada y devuelve un número mayor que 0".
• No recibe nada, paréntesis vacíos: def obtieneYValidaDatosDeEntrada():
• Devuelve un número: acaba con return num.
• Dentro va la validación de siempre: pedir, while mientras sea incorrecto, volver a pedir.
8. Reglas para el examen
1.  Todas las funciones arriba, el programa principal abajo. Si llamas a una función antes de definirla, da error.
2.  Definir no ejecuta. Si no llamas a la función, no hace nada.
3.  Si la función devuelve algo, guárdalo en una variable al llamarla: res = esMultiplo(num1, num2).
4.  return devuelve, print solo pinta.
5.  Un return devuelve una sola cosa. Para varios valores, usa una lista: return [a, b].
6.  Las variables creadas dentro de una función son solo de la función. Lo que necesite, se lo pasas por parámetro, y lo que saques, lo sacas con return.
7.  Los input() del programa principal van abajo, junto a la llamada. Dentro de la función solo si el enunciado dice que la función pide el dato (como el ejercicio 1).