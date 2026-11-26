def cargaLista():
    lista = [1,2,7,8,2]
    return lista
    
def calculaPares(lista):
    listaPares = []
    for nPar in lista:
        if nPar %2==0:
           listaPares.append(nPar) 
    return listaPares
    
def calculaNegativos(lista):
    listaNegativos = []
    for nNegativo in lista:
        if nNegativo < 0:
            listaNegativos.append(nNegativo)
    return listaNegativos
    
def calculaSuma(lista):
    suma = 0
    for elemento in lista:
        suma = elemento + suma
    return suma

def calculaMedia(lista):
    sumaNum = calculaSuma(lista)  
    media = sumaNum / len(lista)
    return media
    
def inicializaMenu():
    print("====MENU===")
    print("Pulsa [a] si deseas consultar la media: ")
    print("Pulsa [b] si deseas saber los nº pares: ")
    print("Pulsa [c] si deseas saber los nº negativos: ")
    print("Pulsa [d] si deseas calcular la suma: ")
    menu = input("Introduce una letra para acceder al menu: ").lower()
    match menu:
            case "a":
                media = calculaMedia(lista)
                print(media)
                    
            case "b":
                numPares = calculaPares(lista)
                print(numPares)
                
            case "c":
                numNegativos = calculaNegativos(lista)
                print(numNegativos)
                
            case "d":
                total = calculaSuma(lista)
                print(total)
                
lista = cargaLista()
opcion = inicializaMenu()

