while True :
     print ("hola Mundo")
     if input("continuar? [si/no]:  ") == "no":
        break


# Con continue

salir = True
i = 0
while salir:
    print(f"Estoy al principio de la iteracion : {i}:")
    i += 1
    if input("ir a la proxima iteracion? [si/no]") =="si":
        continue
    if input("Desea salir ? [si/No]") == "si":
     salir = False
    print(f" estoy al final de la iteracion: {i-1}")
    
    