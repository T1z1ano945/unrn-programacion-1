"""Pedir una edad por teclado. Antes de usarla como numero, revisar que el dato tenga sentido.

El programa tiene que aceptar edades numericas entre 0 y 120. Si la persona escribe espacios de mas, el programa deberia poder limpiarlos antes de validar.

Si el dato sirve, mostrar algo como:

Edad registrada: 25

Si no sirve, mostrar un mensaje de error claro. No alcanza con que el programa se rompa."""

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]

Nombres_normalizados = []

for N in nombres:
    nombre = N.strip().capitalize()
    Nombres_normalizados.append(nombre)

print(Nombres_normalizados)