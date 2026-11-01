#Pide fecha actual
dia = int(input("Introduce un número (1-31): "))
mes = input("Introduce un mes: ").upper()
#pida un hemisferio (Norte/Sur). 
# Si se introduce un valor incorrecto, el programa volverá a pedir que se introduzca un hemisferio
hemisferio = input("Introduce un hemisferio(Norte o Sur): ").upper()
while hemisferio != "NORTE" and hemisferio != "SUR":
    print("Hemisferio incorrecto")
    hemisferio = input("Vuelve a introducir un hemisferio(Norte o Sur): ").upper()
if (hemisferio == "NORTE") and (mes =="SEPTIEMBRE" and dia < 24):
    print("Otoño")
if (hemisferio == "NORTE") and (mes =="DICIEMEBRE" and dia < 22):
    print("Invierno")
if(hemisferio == "NORTE") and (mes =="MARZO" and dia < 22):
    print("Primavera")   
if(hemisferio == "NORTE") and (mes =="JUNIO" and dia < 22):
    print("Verano")     

if (hemisferio == "SUR") and (mes =="SEPTIEMBRE" and dia < 24):
    print("Otoño")
if (hemisferio == "SUR") and (mes =="DICIEMEBRE" and dia < 22):
    print("Invierno")
if(hemisferio == "SUR") and (mes =="MARZO" and dia < 22):
    print("Primavera")   
if(hemisferio == "SUR") and (mes =="JUNIO" and dia < 22):
    print("Verano")  


listaDias=[31,28,31,30,31,30,31,31,30,31,30,31]
listaMes=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


#while dia < 32  or mes < 13:
    #if 
#while mes in listaMes:
    #mes


