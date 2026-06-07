"""Pedir al usuario un codigo de materia con este formato:

PROG-101
El programa tiene que validar que:

tenga un solo guion -;
la parte de la izquierda tenga solo letras;
la parte de la derecha tenga solo numeros.
Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo upper).

Ejemplo:

Codigo valido: PROG-101

Si no es valido, mostrar un mensaje de error claro."""

Codigo_de_materia = input("Ingrese el codigo de alguna materia, ( formato: 4 letras - 3 numeros ): ")

Codigo_corregido = Codigo_de_materia.strip()
if Codigo_corregido.count("-") == 1:
    parte_de_letras,parte_de_numeros = Codigo_corregido.split("-")

    if parte_de_letras.isalpha() and parte_de_numeros.isnumeric():
        print(f"El Codigo es valido: {Codigo_corregido.upper()}")
    else:
        print(" El formato es incorrecto. Solo puede contener letras de la parte izquierda y numeros en la parte derecha")

else:
    print("Debe contener un Guion (-) entre medio de las letras y numeros")






