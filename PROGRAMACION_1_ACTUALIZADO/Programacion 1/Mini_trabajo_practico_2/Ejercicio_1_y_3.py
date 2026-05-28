#En este caso hice el ejercicio 1 y 3 solamante que utilice input

Edad = int(input("Introduce tu edad: "))
Documento_obligatorio = input("Tienes documento s/n (Pon las leetras en miniuscula): ")
if Edad >= 18 and Documento_obligatorio == "s":
    print(f"Tienes {Edad}, y tienes tu documento por ende puedes entrar")

elif Edad >= 18 and Documento_obligatorio == "n":
    print(f"Tienes la mayoria de edad debido a que tienes {Edad}, pero no tienes tu documento por ende no puede pasar")

else:
    Edad < 18
    print(f"Tienes { Edad}, eres menor de edad y aunque tengas o no tu documento no te puedo dejar pasar")
