numero = int(input(" Introduce el numero: "))

if numero % 2 == 0 and numero < 10:
    print("El numero es par y es menor a 10")

elif numero % 2 == 0 and numero > 10:
    print(" El numero es par y es mayor a 10 ")

else:
    print("El numero es impar")


