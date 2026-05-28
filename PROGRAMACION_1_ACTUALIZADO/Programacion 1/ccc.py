linea = " mara ; programacion ; 8 "

partes = linea.split(";")
print(partes)
nombre = partes[0].strip().capitalize()
print(nombre)
materia = partes[1].strip().capitalize()
print(materia)
nota_texto = partes[2].strip()

if nota_texto.isnumeric():
    nota = int(nota_texto)
    print(f"{nombre} cursa {materia} y obtuvo {nota}")
else:
    print("La nota no es valida")