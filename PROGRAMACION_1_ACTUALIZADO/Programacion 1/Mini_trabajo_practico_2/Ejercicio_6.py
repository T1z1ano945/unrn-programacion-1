Clave_ingresada = (input("Introduce la clave: "))
Clave_almacenada = "3434"
Tiene_token = (input(" Tienes token ? s/n "))

if Clave_almacenada == Clave_ingresada :
    print("Acceso permitido")

elif Clave_almacenada != Clave_ingresada and Tiene_token == "s":
    print("La clave no es la misma pero como tienes token puedes acceder")

else:
    print("La clave no es la misma y tampoco tienes token, lo siento no puedes acceder")