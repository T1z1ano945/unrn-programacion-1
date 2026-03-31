"""En base al ejercicio anterior, crear un nuevo programa donde la lista pueda tener un maximo de 5 elementos.

Condiciones:

Si el usuario escribe "fin", el programa termina.
Si la lista llega a 5 elementos, el programa ya no debe seguir agregando datos.
Al finalizar, mostrar la lista y su cantidad de elementos."""





Lista_de_colores = []

ingresa_colores = "aca empieza"

cantidad_de_elementos = 0

while  ingresa_colores != "fin" and cantidad_de_elementos < 5:
    ingresa_colores = input("ingresa un color: ")
    
    
    if ingresa_colores != "fin":
        Lista_de_colores.append(ingresa_colores)
        cantidad_de_elementos = cantidad_de_elementos + 1
    else:
        print("Haz puestoo fin lo sentimos")
        
print(f"Los colores son : {Lista_de_colores} y la cantidad de elementos son: {len(Lista_de_colores)}")
