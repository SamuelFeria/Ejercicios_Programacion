n = int(input("Dame un numero: "))
filaPrimeraYUltima = "*" + (n-2) * "0"  + "*"
filaIntermedia = "*"+ (n//2 +1) * "#" + "*"
filaOtras= "*@"+"*"
for i in range(n):
    if i == 0 or i == n-1:
        print(filaPrimeraYUltima)
    elif i:
        print (filaIntermedia)        
    else:
        print(filaOtras)
     
