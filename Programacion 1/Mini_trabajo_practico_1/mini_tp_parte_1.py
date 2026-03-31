# Parte 1: Exploracion en el interprete

#1)

print("hola mundo")

#2)

print("hola Tiziano como estas ?")

#3)

a = 3
b = 5

sumatoria = a + b 
resta = a - b
multiplicacion = a* b
division = a/b

print(resta)
print(sumatoria)
print(multiplicacion)
print(division)

#4)

a = float(2.5)
b = float(3.4)

sumatoria_float = a + b
resta_float = a - b

print (sumatoria_float)
print(resta_float)

#5) 

a = 1
b = 2
b1 = 2.0

sumatoria = a + b
sumatoria1 = a + b1

print(sumatoria)
print(sumatoria1)

#6)

a = 10
b = 3

operacion = a // b #-----> Esto representa el resultado de la operacion en este caso (division) pero redondeado hacia abajo
operacion1 = a % b # -----> Esto representa el resto de la operacion

print(operacion)
print(operacion1)

#7)

#print("hola")# ---> si omitimos un parentesis el programa detectara que nunca se cerro  dejandonos como mensaje (Was never closed)
#print " hola" # ---> en esta caso si nos falto poner los dos parentesis el programa nos indicara un syntax error,dandonos un consejo (Did you mean print(..))

#8)

segundos = 60
minutos_dados = 42
segundos_dados = 42

segundos_calculados = (segundos * minutos_dados) + segundos_dados

print(f"En 42 minutos y 42 segundos hay {segundos_calculados} segundos")