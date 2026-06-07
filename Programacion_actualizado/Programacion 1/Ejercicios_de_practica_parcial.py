"""
# ejercicio 1
entero = 32
flotante = 3.23
booleano = True
string = "Hola"
tupla = 3,4
print(f"valor de variable: {entero} Tipo: {type(entero)}")
print(f"Valor de variable: {flotante} Tipo: {type(flotante)}")
print(f"Valor de variable: {booleano} Tipo: {type(booleano)}")
print(f"Valor de variable {string} Tipo {type(string)}")

# ejercicio  2 

nums = [1,100,300,1000]
cantidad_de_elementos = 0
suma_total = 0

for numero in nums:
    cantidad_de_elementos = cantidad_de_elementos + 1
    suma_total = suma_total + numero
    promedio = suma_total / cantidad_de_elementos

print(f"La suma total es: {suma_total}, la cantidad de elementos son: {cantidad_de_elementos} y su promedio es: {promedio}")

# ejercicio 3

x = [10,-1,2,3,5,7,6,-7,8,-10,30,-40]

numero_maximo = 0
numero_minimo = 0

for numero in x:
    if numero > numero_maximo:
        numero_maximo = numero

    elif numero < numero_minimo:
        numero_minimo = numero

print(f"El numero maximo es {numero_maximo} y el numero minimo es: {numero_minimo}")

# ejercicio 4

nums = [10,-1,2,3,5,7,6,-7,8,-10,30,-40]

for numero in nums:
    if numero % 2 == 0:
        print(f"Este numero es par ({numero})")
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
nums = [10,-1,2,3,5,7,6,-7,8,-10,30,-40]

for numero1 in range(len(nums)):
    if nums[numero1] % 2 == 0:
        print(f" Este numero es par: {nums[numero1]}")

# ejercicio 4.1
lista_de_numeros_sin_numeros_repetidos = []
nums = [1,2,2,3,4,4,4,5]

for numero in nums:
    if numero not in lista_de_numeros_sin_numeros_repetidos:
        lista_de_numeros_sin_numeros_repetidos.append(numero)

print(f"La lista de numeros sin repetetir son {lista_de_numeros_sin_numeros_repetidos }")


# ejercicio 5 
productos = ["papa", "manzana", "Zanahoria","Manzana"]
cantidad_de_productos = 0

for producto in productos:
    cantidad_de_productos = cantidad_de_productos + 1

print(f" El primer elementos de la lista es: {productos[0]}, el ultimo elemento de la lista es: {productos[3]} y la cantidad de productos es: {cantidad_de_productos}")

# ejercicio 6

def saludo():
    print("Hola ¿ como estas ?")

def saludo1():
    return "Hola ¿ como estas ?"

def  saludo_perzonalizado ( nombre ):
    return f"Hola ¿ como estas {nombre} ?"


saludo()

print(saludo1())

print(saludo_perzonalizado("Tiziano"))

# ejercicio 7
def saludo():
    return "Hola"
print(saludo())

def saludo():
    print(" hola")
print(saludo())


# ejercicio 8
numero = int(input("Ingrese numeros, con la tecla (0) canecela la accion: "))
suma_total = 0
contador = 0
while numero != 0:
    suma_total = suma_total + numero
    contador = contador + 1
    numero = int(input("Ingrese numeros, con la tecla (0) canecela la accion: "))

print(f"La cantidad de numeros inngresados son {contador}, la suma total de estso numeros es {suma_total}, y su pomedio es { suma_total / contador}")

# ejercicio 9

numeros = int(input("Ingrese numeros hasta que aprete la tecla 0: "))
numero_maximo = numeros
numero_minimo = numeros
while numeros != 0:

    if numeros > numero_maximo:
        numero_maximo = numeros
    elif numeros < numero_minimo:
        numero_minimo = numeros
    numeros = int(input("Ingrese numeros hasta que aprete la tecla 0: "))
    

print(f" El numero minimo es {numero_minimo} y el numero maximo es { numero_maximo}")


# ejercicio 10
lista_de_productos = []
nombres_de_productos = input("ingrese la cantidad de productos, ingresa la palabra (fin) para finalizar: ")
cantidad_de_productos = 0

while nombres_de_productos != "fin":
    lista_de_productos.append(nombres_de_productos)
    cantidad_de_productos = cantidad_de_productos + 1
    nombres_de_productos = input("ingrese la cantidad de productos, ingresa la palabra (fin) para finalizar: ")

print(f" La cantidad de productos es: {cantidad_de_productos}, el primer elemento de la lista es: {lista_de_productos[0]} y el ultimo elemento de la lista es: {lista_de_productos[-1]}")
    
"""
# ejercicio 11
"""
def obtener_precio(producto):
    if producto == "martillo":
        return 3000
    elif producto == "clavos":
        return 500
    elif producto == "destornillador":
        return 1500
    else:
        return 0
    
productos_unicos = []
suma_total = 0
producto = input("Ingrese productos: para finalizar ponga la palabra (fin): " )

while producto != "fin":
    if producto not in productos_unicos:
        productos_unicos.append(producto)
    suma_total = suma_total + obtener_precio(producto)
    producto= input("Ingrese productos: para finalizar ponga la palabra (fin): " )

    

print(f"Productos unicos ingresados {productos_unicos}")
print(f" total final {suma_total}")

"""



nums = [2,-1,-3,-5,25]
multiplicacion = 1

for numero in nums:
    if numero > 0:
        multiplicacion = multiplicacion * numero


print(f" la multiplicacion de los numeros psoitivos es {multiplicacion}")