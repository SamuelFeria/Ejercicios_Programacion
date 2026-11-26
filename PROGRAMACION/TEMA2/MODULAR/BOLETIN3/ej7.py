def construyeSinRepetidas(lista):
    listaSinRepeticion = []
    for palabra in lista:
        if palabra not in listaSinRepeticion:
                listaSinRepeticion.append(palabra)
    return listaSinRepeticion

lista = ["hola", "adios", "como","hola"]
listaSalida = construyeSinRepetidas(lista)
print(listaSalida)


    