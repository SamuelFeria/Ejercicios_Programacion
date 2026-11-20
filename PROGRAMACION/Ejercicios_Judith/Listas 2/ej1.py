#Pokédex (listas): pide por teclado 5 nombres de Pokémon, guárdalos en una lista y muestra la lista, el primero, el último y cuántos hay.
lista_pokemons = []
numVeces = 5
for i in range(numVeces):
    nombre_pokemon = input("Introduce el nombre del pokemon: ")
    lista_pokemons.append(nombre_pokemon)
print(lista_pokemons,"primer pokemon de la lista:",lista_pokemons[0],"|","ultimo pokemon de la lista:",(lista_pokemons[-1]),"|","total de pokemons:",len(lista_pokemons))