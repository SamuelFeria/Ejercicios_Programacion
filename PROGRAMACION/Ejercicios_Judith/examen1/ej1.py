#Tarifa de envío. Pide el peso del paquete en kilos (entero) y si es urgente (s o n). Hasta 1 kg incluido cuesta 5; de más de 1 hasta 5 kg incluidos, 8; más de 5 kg, 12. Si es urgente, se suman 3. Escribe Precio: seguido del precio.
peso_paquete = int(input("Introduce el peso del paquete: "))
urgente = input("¿El envio es urgente?('s' si es urgente, 'n' si no es urgente): ").upper()
precio_urgente = 3
if urgente == "S" and peso_paquete <=1:
    precio = 5 + precio_urgente
    
elif urgente == "N" and peso_paquete <=1:
    precio = 5 
    
elif urgente == "S" and peso_paquete > 1 and peso_paquete >=5:
    precio = 8 + precio_urgente
   
elif urgente == "N" and peso_paquete > 1 and peso_paquete >=5:
    precio = 8
    
elif urgente == "S" and peso_paquete >5:
    precio = 12 + precio_urgente
    
elif urgente == "N" and peso_paquete >5:
    precio = 12

print("El envio cuesta:",precio)




