grupo1=input("Introduce un grupo sanguíneo: ").upper()
grupo2=input("Introduce un grupo sanguíneo: ").upper()
listaDonaA=["A", "AB"]
listaRecibeA=["0", "AB"]
if grupo1 =="A":
    if grupo2 == "A" and grupo2 in listaDonaA:
        dona= True
    if grupo2 in listaRecibeA:
        recibe = True
print("El grupo: ", grupo1 +"dona a", grupo2, "?", dona)



