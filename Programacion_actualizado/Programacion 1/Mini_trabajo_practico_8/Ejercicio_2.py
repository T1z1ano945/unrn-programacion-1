# Ejercicio 2:
"""Dada la siguiente lista de tuplas:

mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]
Cada tupla tiene el formato:

(tipo_medicion, valor, ubicacion)
Escribí un programa que:

Cree un diccionario donde la clave sea la ubicación.
Cada ubicación debe guardar una lista con sus mediciones.
Cree un conjunto con todos los tipos de medición sin repetir.
Muestre el diccionario final.
Muestre el conjunto de tipos encontrados."""

mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

Diccionario_con_las_mediciones = {}

tipos_unicos_de_medicion = set()

for tipo_med, valor_med, ubicacion in mediciones:
    lista = []
   # print(tipos_unicos_de_medicion)
    if ubicacion not in Diccionario_con_las_mediciones:
        Diccionario_con_las_mediciones[ubicacion] = lista
    Diccionario_con_las_mediciones[ubicacion].append((tipo_med,valor_med))
    tipos_unicos_de_medicion.add(tipo_med)
    #print(tipos_unicos_de_medicion)


print(f"Diccionario_de_datos: {Diccionario_con_las_mediciones}")
print(f"Tipos_de_mediciones: {tipos_unicos_de_medicion}")




# Utilice print para verfiicar que el codigo este bien.









