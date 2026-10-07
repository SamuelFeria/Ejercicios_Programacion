operacionesBasicas = input("Escribe un operador basico: [+ , - , / , *] :")
num1 = int (input("Escribe un número :"))
num2 = int (input("Escribe otro número :"))
match operacionesBasicas:
    case "+":
        resultado = (num1 + num2)
    case "-":
        resultado = (num1 - num2)
    case "*":
        resultado = (num1 * num2)
    case "/":
        resultado = (num1 / num2)
    case _:
        resultado = "No es un operador válido"
print(resultado)


