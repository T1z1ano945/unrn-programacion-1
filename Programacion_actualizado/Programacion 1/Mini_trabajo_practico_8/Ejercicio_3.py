# Ejercicio 3:
"""Ejercicio 3 — Base de datos de alumnos
Escribí un programa que:

Pida al usuario el nombre de 4 alumnos.
Valide que el nombre no esté vacío.
Guarde los nombres válidos en una lista.
Escriba los nombres en un archivo llamado alumnos.txt, un nombre por línea.
Cierre el archivo."""

alumnos = []
contador = 0

while contador < 4:
    nombre_de_alumno = input(" Ingrese cuatro nombres: ")
    if nombre_de_alumno != "":
        alumnos.append(nombre_de_alumno)
        contador = contador + 1
        
    else:
        print("Perdon pero el nombre no puede estar en vacio.")

Archivo_de_alumnos = open("alumnos.txt", "w")

for nombre in alumnos:
    Archivo_de_alumnos.write(f"{nombre}\n")

Archivo_de_alumnos.close()

print("El archivo se guardo exitosamente")