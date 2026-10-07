pedido = float (input ("Intorduce precio "))
tieneCuponActivo = int (1)
if pedido >= 20 and tieneCuponActivo > 0:
        print( pedido - pedido / 10)
else:
    print (pedido , ", No tienes descuento, porque no superas los 20€. ")
