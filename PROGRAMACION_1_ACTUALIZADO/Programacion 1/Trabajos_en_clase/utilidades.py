precio_de_hamburguesa = 100
precio_de_milanesa = 125
precio_de_pizza = 140


def pedir_comida():
    comida = ""
    while comida == "":
        comida = input("ingresa tu comida: ").lower()
        return comida



def obtener_precio(comida):
    
    if comida == "hamburguesa":
         comida = print(f"{comida} su valor es de {precio_de_hamburguesa} libras esterlinas")
         return precio_de_hamburguesa

    elif comida == "pizza":
        comida = print (f"{comida} su valor es de {precio_de_pizza} libras esterlinas")
        return precio_de_pizza
    
    elif comida == "milanesa":
        comida =  print (f"{comida} su valor es de {precio_de_milanesa} libras esterlinas")

        return precio_de_milanesa
    
    else: 
         print("No hay buscar en otro lado")
         return 0
    
comida = pedir_comida()

print(obtener_precio(comida))