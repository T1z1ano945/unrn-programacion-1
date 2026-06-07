"""contraseña_registrada = "12345"
contraseña_correcta = False

while contraseña_correcta == False:
    contraseña_ingresada = input("Ingresa la contraseña: ")
    
    
    if contraseña_ingresada ==contraseña_registrada:
        contraseña_correcta = True


print( "Acceso permitido")

print("Autodestuyendo el sistema......")"""

""" contador = 1

while contador <= 5:
    print(contador)
    contador = contador +1
    input("Aprete")

print("Se termino el programa adios") """

"""numero = -1

while numero < 0:
    numero = int(input("Ingresar un numero valido: "))

print("Numero valido ingresado")
"""

opcion = ""
print("Puedes elegir entre pizzas, hamburguesas,empanadas")
print("Selecciona la comida para llevar")
print("El comando para salir es terminar pedido")

while opcion != "terminar pedido":
    opcion = input("Esciba la comida que quieres agregar al pedido: ").lower()
    if opcion == "pizza".lower():
        print("Excelente ! Agregamos pizza a su pedido")
    
    elif opcion == "hamburguesas".lower():
        print("Excelente agregamos hamburgesas a su pedido")

    elif opcion == "empanadas".lower():
        print("Excelente agregamos empanadas a su pedido")
    
    elif opcion == "terminar pedido":
        print("Cerrando pedido")

    else:
        print(f"Lo siento no tenemos{opcion},prueba otra cosa ")