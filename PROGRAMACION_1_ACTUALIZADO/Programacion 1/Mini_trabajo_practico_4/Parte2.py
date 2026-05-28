"""Escribir una funcion llamada calcular_descuento que reciba un precio.

Condiciones:

Si el precio es mayor a 10000, devolver el precio con 10% de descuento.
Si no, devolver el mismo precio.
Mostrar el resultado final con un mensaje descriptivo."""

def calcular_descuento():
    precio = int(input("Escriba su numero: "))

    if precio >= 10000:
        descuento = precio * 0.10
        print(f"Su precio tiene un descuento del 10 % ")

        return descuento
    else:
        print(f"Su precio es: {precio}")
        return precio


calcular_descuento()

#Ejercico


def obtener_estado(nota):
    if nota >=8:
        return "Prommociona"
        
    elif nota >= 6 and nota <=7:
        return "Aprueba"

    elif nota <6:
        return "Desaprueba" 

print(obtener_estado(3))

