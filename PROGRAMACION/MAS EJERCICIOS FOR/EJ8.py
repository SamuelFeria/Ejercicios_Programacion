n = int(input("introduce un numero: "))
linea = ""
for i in range (n):
    if i %2==0:
        print ("*" + (n-2) * "#"  + "*")
    elif n %2 ==1:
        print((n//2)*"*@"+"*")
    else:
        print((n//2)* "*@")
     
