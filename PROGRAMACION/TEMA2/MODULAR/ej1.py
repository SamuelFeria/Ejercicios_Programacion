# def nombreFuncion (parametro1, parametro2, parametro3)
def calculaSubcadena(cadena,posInicio,posFin):
    subcadena= cadena[posInicio:posFin+1]
    print(subcadena)
  
    
cadena = input("Dame una cadena con 4 caracteres: ")
while len(cadena) < 4:
    cadena = input("Dame una cadena con 4 caracteres: ")
#cajita leer y validar cadena
numero = int((input("Introduzca un número: ")))
if numero %2==0:
    calculaSubcadena(cadena,2,4)
#cajita si cadena es par y multiplos de 2
elif numero %3==0:
    calculaSubcadena(cadena,1,2)
#cajita si cadena es impar y multiplos de 3
elif numero %7==0: 
    calculaSubcadena(cadena,0,3)
#cajita si cadena es multipo de 7


