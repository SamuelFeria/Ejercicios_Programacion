num = int (input("Escribe un número :"))
factorial = 1
texto = ""
for numVeces in range (num,0,-1):
    texto="*"+str(numVeces)+texto
    factorial = factorial * numVeces 
      
    #imprime 5!= 1*2*3*4*5
print(1,texto)
print (num,"!=", factorial)