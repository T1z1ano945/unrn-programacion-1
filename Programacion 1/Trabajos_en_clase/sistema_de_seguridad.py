Contraseña_ingresada = input("ingrese la contraseña: ")
contraseña_almacenada = "12345"
uso_clave_token = bool(input("Usa clave token ? ") == "Si")

if contraseña_almacenada == Contraseña_ingresada:
    print("Acceso permitido")

elif uso_clave_token:
    print("Acceso permitido")

else:
    print("Acceso denegado")

print("gracias por su compra")