#Tienes numeros = [10, 20, 30, 40]. Inserta el 25 entre el 20 y el 30, añade el 50 al final, elimina el 10 y escribe la lista.
numero = [10,20,30,40]
numero.insert(2,25)
numero.append(50)
#con pop eliminamos por posicion y con remove borramos valores numero.remove(10)
numero.pop(0)
print(numero)