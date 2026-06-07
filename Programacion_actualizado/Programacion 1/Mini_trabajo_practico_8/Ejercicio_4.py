diccionario_de_ciudades = {
}

archivo_de_temp = open("temperaturas.txt", "r")

for i in archivo_de_temp:
    i = i.strip()
    partes = i.split(";")
    ciudad = partes[0]
    temperaturas = int(partes[1])
    if ciudad not in diccionario_de_ciudades:
        diccionario_de_ciudades[ciudad] = []
    diccionario_de_ciudades[ciudad].append(temperaturas)

archivo_de_temp.close()

print(diccionario_de_ciudades)
    