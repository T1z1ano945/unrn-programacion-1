Edad = input("Ingresa la edad: ") 
Edad_corregida = Edad.strip()
if Edad_corregida.isnumeric():
    Edad_corregida= int(Edad_corregida)
    if 0<= Edad_corregida <= 120:
        print(f"Edad ingresada: {Edad_corregida}")
    else:
        print("La Edad ingresada es invalida")

" Profe aca tengo una duda aca el strip lo puedo poner en el input ? osea en vez de crear otra variable."