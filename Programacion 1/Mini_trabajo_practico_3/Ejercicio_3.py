""" Escribir un programa que:

Cree una lista vacia.
Pida al usuario que ingrese un elemento.
Agregue ese elemento a la lista.
Repita el proceso hasta que el usuario escriba "fin".
Al finalizar, mostrar:

La lista completa.
La cantidad de elementos ingresados."""

Lista_de_animales = []
ingresa_animales = ""

while ingresa_animales != "fin":
    ingresa_animales = input("Ingresa un animal: ")
    if ingresa_animales != "fin":
        Lista_de_animales.append(ingresa_animales)

print(f" Los animales que me nombraste fueron estos {Lista_de_animales} y la cantidad de elementos son: {len(Lista_de_animales)}")