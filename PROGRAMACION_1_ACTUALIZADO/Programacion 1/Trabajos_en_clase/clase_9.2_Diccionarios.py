#Diccionario:

mi_primer_diccionario = {"Clave_1": "Valor_1",
                         "Clave_2": "Valor_2"}

print(mi_primer_diccionario)
print(type(mi_primer_diccionario))

# Comparamos los casos de uso de una tupla vs un diccionario:

alumno_tupla = ("Paula", "perez", 8)
print(alumno_tupla[2])

alumno_dict = {"Nombre": "Paula",
               "Apellido": "Sanchez",
               "Nota": 8}

print(alumno_dict["Nota"])

# Ejemplos:

#Crear un diccionario

persona = {
    "Nombre": "Martin",
    "Edad": 20
}

#Acceder a un valor usando su clave:
print(persona["Nombre"])

#Modificar un valor existente:

persona["Edad"] = 21

print(persona)

# Agregar una nueva clave:

persona["Ciudad"] = "Bariloche"

print(persona)

# Preguntar si existe una clave 

print("Ciudad" in persona)

# Obteniendo las claves:

keys = persona.keys()

print(keys)

# Obteniendo los valus:

Values = persona.values()

print(Values)

# Recorrer los diccionarios:

#Ejemplos:

persona ={"nombre": "tiziano",
          "edad": "21",
          "ciudad":"Bariloche"
}

# Recorrer por claves: 
for clave in persona:
    print(clave,persona[clave])

# Recorre por clave y valor:

for clave, valor in persona.items():
    print(clave, valor)

# Recorrer solo las claves:

for clave in persona.keys():
    print(clave)

# Recorre solo los valores

for valores in persona.values():
    print(valores)

# Ejericicios:
#3)
#crear un diccionario que reperesnte un producto con:
# ° Nombre 
# ° precio
# ° stock

"""Luego:
1) Mostrar el producto completo.
2) Aumnetar el precio en un 10 %.
3) Restar una unidad al stock.
4) Mostrar un mensaje al final con este formato:
Producto:Nombre-Precio actualizado:precio-stock restante: Stock""" 

Producto = {"Nombre": "Lapiceras",
             "Precio": 2000,
             "Stock": 50}

#print(Producto)

Producto["Precio"] *= 1.10

#print(Producto)

Producto["Stock"] -= 1
#print(Producto)

print(f"Producto: {Producto['Nombre']} - Precio_actualizado: {Producto['Precio']} - Stock_restante: {Producto['Stock']} ")

#4)

Cuenta_de_usuario = {"usuario": "TizianoUlloa",
                     "email": "Salamin34@gmail.com",
                     "Activo": True }

print(Cuenta_de_usuario["email"])

Cuenta_de_usuario["Activo"] = False

print(Cuenta_de_usuario["Activo"])

Cuenta_de_usuario["ultimo_login"] = (6, 5 , 2026)

print(Cuenta_de_usuario)