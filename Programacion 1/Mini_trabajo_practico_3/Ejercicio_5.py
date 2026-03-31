""" Dada una lista, mostrar todos sus elementos usando while.

Ejemplo:

lista = ["pizza", "empanadas", "hamburguesa"]
Salida esperada:

1. pizza
2. empanadas
3. hamburguesa"""


lista = ["Pizza", "empanadas","Hamburguesa"]
contador = 0

while contador < len(lista):
    print(f"Elemento {contador}: {lista[contador]}")
    contador = contador + 1