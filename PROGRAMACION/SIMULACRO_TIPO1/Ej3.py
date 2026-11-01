grupo1=input("Introduce un grupo sanguíneo: ").upper()
grupo2=input("Introduce un grupo sanguíneo: ").upper()
listaDonaA=["A", "AB"]
listaRecibeA=["0", "A"]
listaDonaB=["B", "AB"]
listaRecibeB=["B", "0"]
listaDonaAB=["AB"]
listaRecibeAB=["A","B","AB","0"]
listaDona0=["A","B","AB","0"]
listaRecibe0=["0"]
dona = False
recibe= False
if grupo1 =="A":
    if grupo2 == "A" and grupo2 in listaDonaA:
        dona= True
    if grupo2 in listaRecibeA:
        recibe = True

if grupo1 =="B":
        if grupo2 =="B" and grupo2 in listaDonaB:
             dona=True
        if grupo2 in listaRecibeB:
             recibe=True

if grupo1 =="AB":
        if grupo2 =="AB" and grupo2 in listaDonaB:
             dona=True
        if grupo2 in listaRecibeB:
             recibe=True

if grupo1 =="0":
        if grupo2 =="0" and grupo2 in listaDonaB:
             dona=True
        if grupo2 in listaRecibeB:
             recibe=True

print("El grupo: ",grupo1 +" dona a", grupo2, "?", dona)
print("El grupo: ",grupo1 +" recibe", grupo2, "?", recibe)



