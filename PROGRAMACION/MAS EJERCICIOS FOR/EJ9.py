n = int(input("Dame un numero: "))
filaPrimeraYUltima = "*" + (n-2) * "0"  + "*"
filaIntermedia = "*"+ (n-2) * "#" + "*"
filaOtras= (n//2)*"*@"+"*"

for i in range(n):
    if i == 0 or i == n-1:
        print(filaPrimeraYUltima)
    elif i==n//2:
        print (filaIntermedia)        
    else:
        print(filaOtras)
     
