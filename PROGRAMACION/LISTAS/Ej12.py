import random
lista=[]
pares=[]
impares=[]
for i in range (20):
    numeroRandom=random.randint(0,100)
    lista.append(numeroRandom)
    if numeroRandom %2==0:
        pares.append(numeroRandom)
    elif numeroRandom %2==1:
        impares.append(numeroRandom)
print(pares+impares)
