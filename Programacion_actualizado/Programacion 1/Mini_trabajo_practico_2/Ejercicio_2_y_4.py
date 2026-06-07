# En este caso hice el ejercicio 2 y 4 solamente que utilice input.

temperatura = int(input(" Pon la tempretura: "))

if temperatura < 10:
    print(f"Uff deberias utilizar abrigo hacen {temperatura} grados")

elif  10 <= temperatura < 20:
    print(f"Deberias utilizar ropa media hacen {temperatura} grados")

elif temperatura >= 20:
    print(f"Deberias utilizar ropa liviana no hace tanto frio hacen {temperatura} grados")