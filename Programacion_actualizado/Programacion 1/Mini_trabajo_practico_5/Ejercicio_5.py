# Diccionario: ficha simple
print("-"*60)
alumno = {
    "Nombre": "Tiziano",
    "Edad": 20,
    "Apellido": "Ulloa"
}
print(alumno)
print(f" Tu nombre es: {alumno["Nombre"]} y tu apellido es: {alumno['Apellido']}")

alumno["Edad"] +=1

print(alumno)

alumno["Activo"] = True

print(alumno)


print("-"*60)
