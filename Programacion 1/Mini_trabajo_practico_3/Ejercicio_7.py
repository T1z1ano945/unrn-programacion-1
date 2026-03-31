"""Armar un sistema simple de pedidos.

El programa debe:

Permitir agregar comidas a una lista.
Aceptar solo estas opciones:
pizza
empanadas
hamburguesa
Si el usuario escribe otra opcion, mostrar un mensaje de error.
Terminar cuando el usuario escriba "terminar".
Al final:

Mostrar el pedido completo.
Mostrar cuantos elementos tiene el pedido."""

lista_comidas = []
comida = ""
print(" Solo puede elegir entre (pizza, empanada,hamburguesa)")

while comida != "terminar":
    comida = input("Elige su pedido: ")

    if comida == "pizza" or comida == "empanada" or comida == "hamburguesa":
        lista_comidas.append(comida)

    elif comida == "terminar":
        print("terminando su pedido.........")
    
    else:
        print("lo sentimos no tenemos eso en el menu")


print(f"Su pedido completo es {lista_comidas} y la cantidad de elementos que tiene es de {len(lista_comidas)}")