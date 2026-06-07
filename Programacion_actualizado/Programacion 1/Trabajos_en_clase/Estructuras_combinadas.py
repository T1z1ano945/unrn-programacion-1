# Listas, tuplas, conjuntos y diccionarios en un solo lugar:
# Ejemplo:

alumno = {
    #str
    "nombre": "Ana",
    #list
    "notas":[8, 6 ,9],
    #tuple
    "Ubicacion": ("Bariloche", "Rio Negro"),
    #Set
    "materias": {"Programacion","Matematica"}
}

nota_total = 0

for nota in alumno["notas"]:
    nota_total = nota_total + nota

print(nota_total)


# LISTAS DE DICCIONARIOS:

# Ejercicio integrador (ejercicio 5)

alumnos = [
    {
        "nombre": "Joaquin",
        "notas": [8, 5, 7],
        "materias": { "Programación", "Matemática"}
    },
    {
        "nombre": "Juan",
        "notas": [4, 3, 2],
        "materias": { "Programación" }
    },
    {
        "nombre": "Lucia",
        "notas": [6, 8, 9],
        "materias": {"Programación", "Inglés"}
    }
]

print("-"*25)

alumnos[0]["materias"].add("Laboratorio")
print(alumnos[0])

print("-"*25)

for alumno in alumnos:
    if "matematica" in alumno["materias"]:
        print(f"{alumno['nombre']} cursa matemarica")


for alumno in alumnos:
    print(alumno["nombre"])

print("-" * 25)

# usando len y sum:
for alumno in alumnos:
    suma_notas = sum(alumno["notas"])
    cantidad_notas = len(alumno["notas"])
    promedio = suma_notas / cantidad_notas

    if promedio >= 4:
        print(f"{alumno["nombre"]} aprobo con un promedio de {promedio}")

    else:
        print(f"{alumno['nombre']}, desaprobo con un promedio de {promedio}")


# usando sin len y sum:

for alumno in alumnos:
    suma_de_notas = 0
    cantidad_de_notas_1 = 0

for nota in alumno["notas"]:
    suma_de_notas = suma_de_notas + nota
    cantidad_de_notas_1 = cantidad_de_notas_1 + 1

promedio_1 = suma_de_notas / cantidad_de_notas_1

print(f"{alumno['nombre']}, aprobo con un promedio de {promedio_1}")