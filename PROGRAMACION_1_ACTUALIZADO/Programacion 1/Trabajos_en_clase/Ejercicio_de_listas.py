"""lista_super = []

lista_super.append("Huevos")
lista_super.append("Pan")
lista_super.append("Azucar")
lista_super.append("Leche")


print(lista_super)
print(lista_super[3])
print(len(lista_super))
print(lista_super[-1])

lista_super.remove("Azucar")

print(lista_super)"""

lista_de_productos = []


cantidad_de_productos = 1

while cantidad_de_productos <= 5:
    productos =(input("Que deseas agregar a la lista?: "))
    lista_de_productos.append(productos)
    cantidad_de_productos = cantidad_de_productos+1
    

print(f"La lista contiene {lista_de_productos} y tiene {len(lista_de_productos)} productos")



    