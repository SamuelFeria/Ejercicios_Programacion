num = float(input("introduce un precio: "))
suma=0
while num >0:
    suma= suma + num
    num = float(input("introduce un precio: "))
iva=0.07
iva = suma *iva
suma = suma + iva
print("El iva es: ", iva)
print("El total es con IVA incluido es : ",suma)