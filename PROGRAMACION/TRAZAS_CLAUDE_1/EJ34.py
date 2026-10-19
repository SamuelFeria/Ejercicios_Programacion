#El usuario introduce, en este orden: 3, 5, 4, 2, 7. 

n = int(input("Número: "))
producto = 1
i = 1
while i <= n:
    producto = producto * i
    i = i + 1
    n = int(input("Número: "))
print("Producto:", producto)