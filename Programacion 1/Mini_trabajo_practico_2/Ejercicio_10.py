dia_0 = "Lunes"
dia_1 = "Martes"
dia_2 = "Miercoles"
dia_3 = "Jueves"
dia_4=  "Viernes"
dia_5 = "Sabado"
dia_6= "Domingo"

for dias in range (0,7):
    if dias == 0:
        print(f"{dias}: {dia_0}")

    if dias == 1:
        print(f"{dias}: {dia_1}")

    if dias == 2:
        print(f"{dias}: {dia_2}")

    if dias == 3:
        print(f"{dias}: {dia_3}")
    
    if dias == 4:
        print(f"{dias}: {dia_4}")

    if dias == 5:
        print(f"{dias}: {dia_5}")
    
    if dias == 6:
        print(f"{dias}: {dia_6}")


dia_0 = "Lunes"
dia_1 = "Martes"
dia_2 = "Miercoles"
dia_3 = "Jueves"
dia_4 = "Viernes"
dia_5 = "Sabado"
dia_6 = "Domingo"

for i in range(7):
    if i == 0:
        dia = dia_0
    elif i == 1:
        dia = dia_1
    elif i == 2:
        dia = dia_2
    elif i == 3:
        dia = dia_3
    elif i == 4:
        dia = dia_4
    elif i == 5:
        dia = dia_5
    else:
        dia = dia_6

    print(f"{i}: {dia}")
