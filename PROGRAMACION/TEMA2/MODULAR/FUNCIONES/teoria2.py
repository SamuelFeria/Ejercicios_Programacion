9. Qué va en la función y qué va en el programa principal
La función calcula y devuelve. El programa principal pide, repite y muestra.
Ejemplo con el ejercicio 9 del boletín, Login:
Qué hace
Dónde va
Comprobar si usuario y contraseña son correctos
Función
Sumar 1 al contador si falla
Función
Devolver el resultado con return
Función
Pedir usuario y contraseña con input
Programa principal
Repetir hasta tres veces (while)
Programa principal
Llamar a la función y guardar lo que devuelve
Programa principal
Mostrar "Bienvenido" o "Has agotado..." con print
Programa principal
Para decidir dónde va cada cosa, lee el enunciado y hazte estas cuatro preguntas:
1.  ¿Qué datos necesita la función? Esos son los parámetros.
2.  ¿Qué tiene que contestar? Eso es lo que va en el return.
3.  ¿Qué se repite? El while o el for y los input van en el programa principal, y la función se llama una vez por vuelta.
4.  ¿Qué se muestra en pantalla? El print va en el programa principal, salvo que el enunciado diga que la función muestre algo.
Excepción: en el ejercicio 1, obtieneYValidaDatosDeEntrada, el enunciado dice que la función lee el dato, y por eso lleva el input dentro.
Las variables de dentro de la función y las del programa principal son cajas distintas, aunque se llamen igual (en el Login, el resultado de la función y el resultadoLogin del programa principal).
10. Módulos y usar funciones de otros ficheros (diapositivas 12 y 13)
Un módulo es un fichero .py que agrupa funciones de un mismo tema. Tu libreria.py con esPar es un módulo. Python ya trae otros: random, math, datetime, sys y os (la diapositiva 12 pide investigar para qué sirven).
Hay tres formas de usar las funciones de otro fichero. Ejemplo con el fichero menuFunciones.py, que tiene las funciones operacionA y operacionB:
Forma
Cómo se escribe
Cómo se llama a la función
Opción 1: importar el fichero
import menuFunciones
menuFunciones.operacionA() (con el nombre del fichero delante)
Opción 2: importar funciones concretas
from menuFunciones import operacionA, operacionB
operacionA() (sin el nombre del fichero)
Importar todas
from menuFunciones import *
operacionA()
La Opción 1 es la que usas en principal.py con libreria.esPar(num).
Reglas:
• El fichero importado tiene que estar en la misma carpeta que el programa.
• Se escribe el nombre del fichero sin .py.
• Si importas con la Opción 1, siempre pones nombreFichero. delante de la función. Si no lo pones, da NameError.
Investiga qué hacen random, math, datetime, sys y os (diapositiva 12). Todas vienen con Python y se usan con import:
Librería
Para qué sirve
Funciones que puedes necesitar
random
Números y elecciones al azar
random.randint(1, 10) da un entero entre 1 y 10, ambos incluidos. random.choice(lista) elige un elemento de la lista. random.shuffle(lista) mezcla la lista.
math
Funciones matemáticas
math.pi, math.sqrt(9) (raíz, da 3.0), math.ceil(3.2) (redondea hacia arriba, da 4), math.floor(3.8) (hacia abajo, da 3).
datetime
Fechas y horas
date.today() es la fecha de hoy. datetime.now() es la fecha y hora de ahora. date(2026, 11, 17).weekday() da el día de la semana, de 0 (lunes) a 6 (domingo).
sys
Cosas del propio programa y del intérprete de Python
sys.exit() termina el programa en ese punto. sys.argv es la lista con los datos que se le pasan al programa al arrancarlo.
os
Cosas del sistema operativo: carpetas y ficheros
os.getcwd() da la carpeta de trabajo. os.listdir(".") lista los ficheros de una carpeta. os.path.exists("fichero.py") dice si existe un fichero.
Ejemplo de uso con las dos formas de importar:
import random, math
from datetime import date

numero = random.randint(1, 10)
print(math.ceil(7 / 2))       # sale 4
print(date.today().year)      # el año actual
math.ceil sirve cuando una división tiene que redondear siempre hacia arriba, por ejemplo "cuántos ataques hacen falta" si sobra algo: 7 / 2 es 3.5 y hacen falta 4.
11. Variables locales y globales (diapositivas 14 a 19)
Una variable puede ser local, si se crea dentro de una función y solo existe ahí, o global, si se crea fuera, en el programa principal.
Tipo
Dónde se crea
Dónde se puede usar
Local
Dentro de la función (los parámetros también son locales)
Solo dentro de esa función
Global
Fuera de las funciones, en el programa principal
Dentro y fuera de las funciones
Una local no se ve desde fuera. Si lo intentas, da NameError:
def saludar():
    saludo = "¡Hola!"
    print(saludo)

saludar()
print(saludo)    # NameError: name 'saludo' is not defined
Una global sí se puede leer dentro de una función (diapositiva 15). En este ejemplo, num2 no es un parámetro, pero la función la ve igualmente:
def operar(a, b):
    multiplica = a * num2    # num2 es global
    print(multiplica)

num1 = 10
num2 = 5
operar(num1, num2)           # sale 50
Si hay una local y una global con el mismo nombre, Python usa primero la local. Son dos cajas distintas con el mismo nombre:
... (181 líneas restantes)