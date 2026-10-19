lista =["andrea", 5, "Pedro", 6,"Lucía", 3 ]
lista[4]="Lucía María"#modifico el valor de la lista en la posicion 4
lista[5]=5 #modifico el valor de la lista en la posicion 5
print(lista [4], ":", lista[5])
numeroElementos= len(lista)
print(lista[numeroElementos-1])
lista.append("Amapro")
lista.append(6)
print(lista)
print(len(lista))

"""print(lista[32])#esto da error porque no existe la posicion 32 en la lista"""