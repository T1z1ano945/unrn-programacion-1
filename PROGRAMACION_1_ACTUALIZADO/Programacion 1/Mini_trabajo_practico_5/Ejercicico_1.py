"""Parte 1 - Teoría
Responder en un archivo de texto plano, con tus palabras, en no más de 4 líneas por punto:

¿Qué es una tupla y en qué se diferencia de una lista?
¿Qué es un conjunto (set) y qué problema resuelve mejor que una lista?
¿Qué es un diccionario y cuándo conviene usar clave-valor?
¿Qué significa combinar estructuras de datos? Dar un ejemplo simple.

1) una tupla es una coleccion ordeanada e inmutable que puede contener distitno tipos de datos, Se diferencia de una lista en que esta no se puede modificar

2) un conjunto es una coleccion desordenada de elementos unicos( sin duplicados), la diferencia principal es que las listas nos permiten elementos duplicados mientras que las listas no ) 

3) un diccionario es una estructura de datos que almacena elementos en forma de pares clave_valor, donde--
clave es unica, inmutable y sirve para acceder rapidamente a un valor asociado.

conviene usar diccionarios cunado se necesita mapear claves de forma eficiente o realizar busquedas rapidas mediante---
el identificador especifico en lugar de por posicion.

4) Cpmbinar estructuras de datos immplica integrar diferentes tips de estructuras desde listas diccionarios etc, para--
aprovechar las ventajas de cada una.

ejemplo claro de estructura combinada:

alumnos = [
    {"nombre": "Paula", "nota": 8},
    {"nombre": "Juan", "nota": 3},
    {"nombre": "Pedro", "nota": 6},
]
print(alumnos)
"""
# Ejercicio 1 Tuplas-Datos_fijos

materia = ("Programacion 1", 3, "Miercoles")

print(materia[0])
print(materia[1])
print(materia[2])

materia,comision,dia = materia

print(materia)
print(comision)
print(dia)
print("-"*25)
# Ejercicio 2 - tuplas: operaciones simples.
#1)
numeros = (4, 7, 2, 9, 7)

print(numeros[0])
print(numeros[-1])

#2)
# con count:
print(f" Cantidad de veces que aparece el 7: {numeros.count(7)} veces")
# sin count:
contador = 0

for x in numeros:
    if x == 7:
        contador = contador + 1

print(f" Cantidad de veces que aparece el 7: {contador} veces")

#3) Ejercicio 3 - sets: basicos.

valores = [3 , 3, 5, 7, 8, 8, 8, 10]

conjunto = set(valores)

print(f"la lista convertida a set es: {conjunto}")

print(f" la cantidad de elementos unicos son: {len(conjunto)}")


