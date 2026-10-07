pedido = int (input (" Introduce precio del pedido: "))
usuario = input ("¿Tienes premium? ¿Si o No?")
if pedido >= 30 or usuario == "Si" :
    print ("No se le aplican los gastos de envio")
print ("Fin")
