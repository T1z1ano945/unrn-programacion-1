#Ejercicio 1

"""Escribir una funcion llamada saludar que reciba un nombre y devuelva un mensaje de bienvenida."""

def saludar(nombre):
    print(f"Hola {nombre } como estas ?")

saludar("tiziano")

# Con input:

def saludar1():
    nombre1 = input("Esciba su nombre: ")
    print(f"Hola {nombre1} bienvenido al sistema")

saludar1()

#Ejercicio 2

"""Escribir una funcion llamada sumar que reciba dos numeros y devuelva el resultado.

Luego:

Guardar el resultado en una variable.
Mostrarlo por pantalla."""

def sumar (a,b):
    return a + b

reslutado = sumar(3, 6)

print(f"El resultado de su operacion es {reslutado}")

# Con input

def sumar1(a,b):
    return a + b

num1 = int(input("Escriba su primer numero: "))
num2 = int(input("Escriba su segundo numero: "))

resultado1 = sumar1(num1, num2)

print(f"El resultado de su operacion es : {resultado1}")

#Ejercicio 3

"""Escribir una funcion llamada es_par que reciba un numero y devuelva True si es par o False si es impar.

Probarla con al menos 3 valores distintos."""

def es_par (numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
print(es_par(4))



