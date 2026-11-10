luchador1 = "Shelly"
luchador2 = "Colt"
tipo_luchador1 = "Tanque"
tipo_luchador2 = "Normal"
vida_luchador1 = int(3100)
vida_luchador2 = int(2000)
dano_luchador1 = int(600)
dano_luchador2 = int(500)
ataque = 0

while vida_luchador1 > 0 or vida_luchador2 > 0:
    ataque = ataque+1
    
    
    vida_luchador1 = vida_luchador1 - dano_luchador2
    vida_luchador2 = vida_luchador2 - dano_luchador1

    if vida_luchador1 < 0:
        vida_luchador1 = 0
        
    if vida_luchador2 < 0:
        vida_luchador2 = 0
        
    
    print("Daño del luchador1: "+ str(dano_luchador1))
    print("Daño del luchador2: "+ str(dano_luchador2))
    print("Vida del luchador1: "+ str(vida_luchador1))
    print("Vida del luchador2: "+ str(vida_luchador2))
if vida_luchador1 == 0 and vida_luchador2 == 0:
    print("Empate")
elif vida_luchador2:
    print("Gana el: ", luchador1,"necesitó",ataque,"y derroto a",luchador2)
else:
    print("Gana el: ", luchador2,"necesitó",ataque,"y derroto a",luchador1)

    


