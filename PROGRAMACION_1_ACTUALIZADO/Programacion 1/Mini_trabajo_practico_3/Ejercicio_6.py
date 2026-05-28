"""Escribir un programa que:

Tenga una lista ya cargada.
Pida al usuario un elemento.
Indique si ese elemento esta en la lista.
Si esta, mostrar en que posicion aparece."""

lista_animales = ["perro","gato","serpiente","leon"]

elemento = input("Escribe un animal: ")

contador = 0

elemento_encontrado = False

while contador < len(lista_animales):
    if lista_animales[contador] == elemento:
        print(f"El elemento si esta en la lista y esta en la posicion: {contador}")
        elemento_encontrado = True
    contador = contador + 1
    
if elemento_encontrado == False:
    print("El elemento no esta en la lista")


