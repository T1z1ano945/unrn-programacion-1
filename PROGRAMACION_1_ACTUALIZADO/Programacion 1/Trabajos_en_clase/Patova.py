edad = int(input("ingrese su edad:"))
Documento = bool(input("tiene documento ?") == "si")

if edad > 18 and Documento:
    print(f"Tenes {edad} años y tienes tu Documento por ende puedes entrar al establecimiento")

elif edad > 18 and Documento == False:
    print(f"eres mayor de edad por que tienes{edad} años , pero como no tenes tu documento no puedes acceder al establecimiento")

else:
    edad < 18 and Documento
    print(f"Eres menor  debido a que tenes {edad} de edad por ende no puedes entrar")





