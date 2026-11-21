#Palabra al revés (cadenas): pide una palabra y muéstrala al revés, sin usar [::-1] ni reverse.
palabra = input("Introduce una palabra: ")
palabra_reves = ""
for i in range (len(palabra)-1,-1,-1):
    palabra_reves = palabra_reves + palabra[i] 
print(palabra_reves)