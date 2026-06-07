# Conjuntos Set:

mi_primer_comjunto = {1,2,3,4,5,6,6,4,0}
print(mi_primer_comjunto)
print(len(mi_primer_comjunto))

print(type(mi_primer_comjunto))

#crear set:

nombres = {"Ana","Camila","Bianca","Brenda"}
print(nombres)

# Agregar con Add

nombres.add("Lucia")

print(nombres)

# Elminar con remove:

nombres.remove("Brenda")
print(nombres)

# Consultar pertenencia con in:

print("Camila" in nombres)

# convertir lista a set para eliminar repetidos:

lista_nombres = ["Ana","Camila","Camila","pedro"]
nombres_unicos = set(lista_nombres)
print(nombres_unicos)

# Ejercicio:

"""Dada una lista de nombres repetidos, mostrar:
- Los nombres unicos
- La cantidad de nombres distintos

Codigo base:
nombres = ["Ana", "Juna", "Ana", "Pedro", "Juan", "Lucia"]
"""
nombres = ["Ana", "Juan", "Ana", "Pedro", "Juan", "Lucia"]

nombres_unicos1 = set(nombres)

cantidad_de_nombres = (len(nombres_unicos1))

print(nombres_unicos1)
print(cantidad_de_nombres)




