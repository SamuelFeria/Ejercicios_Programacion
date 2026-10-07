velocidad = int(input("¿Que velocidad de internet tienes?: "))
planPremium = True
permiteVer4k = planPremium and velocidad > 25
if permiteVer4k:
    print("Puedes ver contenido en 4K")
else:
    print("No puedes ver contenido en 4K")