#Parte 2: Variables y tipos de datos

#1) 

mensaje = ("hola mundo")

print (mensaje)

#2)

nombre = "Tiziano"

apellido = "Ulloa"

print(f"Bienvenido {nombre} {apellido} al mundo Pyton")

#3)

cadena = "Mundo Python"
Entero = 24
Flotante = 2.4

print(type(cadena))
print(type(Entero))
print(type(Flotante))

#4)

numero_entero = int(34)
numero_flotante = float(2.3)

sumatoria = numero_flotante + numero_flotante

print(type(sumatoria))

#5)

meses = 12
años = 20
altura = 1.78 

meses_vividos_aprox = meses * años
edad_dentro_de_10_años =  años + 10
doble_de_mi_altura = altura * 2

print(f"Los meses que viviste aproximadamente son: {meses_vividos_aprox} meses.")
print(f"La edad que vas a tener dentro de 10 años son unos, {edad_dentro_de_10_años} años.")
print(f"El doble de tu altura es: {doble_de_mi_altura} metros")

#6)

Saludo = "Hola Tiziano"
Saludo_repetido = Saludo * 3
print(Saludo_repetido)
Saludo_contado = (len(Saludo_repetido))
print(f"tu nombre tiene {Saludo_contado} letras, mas 3 espacios")

