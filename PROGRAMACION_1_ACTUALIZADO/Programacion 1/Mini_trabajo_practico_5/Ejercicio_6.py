#Diccionarios: recorridos
print("-"* 60)
producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}

for clave in producto.keys():
    print(clave)
print("-"* 60)

for valor in producto.values():
    print(valor)
print("-"* 60)

for clave, valor in producto.items():
    print(clave,valor)
print("-"* 60)
