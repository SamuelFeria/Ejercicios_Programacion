n = int(input("introduce un numero: "))
linea = ""
for i in range (n):
    linea = n * "*"
    if i ==0 or i == n-1:
        print ("*" + (n-2) * "#"  + "*")
    else:
        print(linea)