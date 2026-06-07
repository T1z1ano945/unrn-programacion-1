mi_primera_tupla = ("Tiziano","Ulloa")
mi_segunda_tupla = (1,2,3,4,5,6)


print(mi_primera_tupla)
print(mi_segunda_tupla)
print(type(mi_segunda_tupla)) #-------> vale lo mismo que en la primera tupla

# ------------------------------------------------------------------------------

# Ejemplos: 

#Formas de crear una tupla:

#1er forma:
persona = ("Tiziano", 20)
# 2da forma:
persona1 = tuple(("Ana",20))

print(type(persona1))

#----------------------------------------------------------------------------------

#  Acceder por indice:

print(persona[0])
print(persona[-1])

# ----------------------------------------------------------------------------------

#Desempaquetar datos:

nombre, edad = persona

print( nombre)
print(edad)

# ----------------------------------------------------------------------------------
# Recorrer con un for:
for x in persona:
    print(x)

#------------------------------------------------------------------------------------
# Inmutable: 
"""
persona[0] = "Pablo" --------------------> Esto no se puede debido a que la tupla es inmutable es decir no se puede modificar
"""
#-------------------------------------------------------------------------------------

# ¿ Cuando podemos usar las tuplas:
#° coordenadas geograficas
#° fechas
#° Resultados de una funcion

# Ejemplos:

coordenada = (-41.13, -71.13)

fecha = (5, 5, 2026)

def operaciones(a, b):
    return(a + b, a - b)

suma, resta = operaciones(5, 10)

# --------------------------------------------------------------------------------------------

#Ejercicio de tuple:
# crear una funcion que reciba un nombre y una edad, y devuelva una tupla con:
#- el nombre
#- la edad
# un booleano que indique si es mayor de edad

def datos_personales(nombre, edad):
    mayor_de_edad = False
    if edad >= 18:
        mayor_de_edad = True

    return(nombre, edad, mayor_de_edad)

resultado = datos_personales("tiziano",13)

print(resultado)

#------------------------------------------------------------------------------------------------------


