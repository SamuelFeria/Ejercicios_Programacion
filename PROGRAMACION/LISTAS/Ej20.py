import random
lista=[]
for i in range (20):
    numeroRandom=random.randint(0,100)
    if numeroRandom %2==0:
        lista.append(numeroRandom)
    elif numeroRandom %2==1:
        lista.append(numeroRandom)
print(lista)
