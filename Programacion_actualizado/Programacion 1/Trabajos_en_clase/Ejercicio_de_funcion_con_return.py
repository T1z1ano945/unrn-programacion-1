"""def saludar (nombre):
    return f"Hola {nombre}"
    
print(saludar ("juan"))

saludo = saludar("pepe")
print(saludo)

def sumar (a,b):
    return a+b
resultado = sumar (1,2)
print(resultado)

def es_mayor(edad):
    if edad >= 18:
        return True
    else:
        return False

print(es_mayor(13))
print(es_mayor(20))"""

def trae_documento():
    return input("trae documento [Si/No]") == "si"

def ingresar_edad():
    return(int(input("ingresar edad: ")))

def puede_pasar(documento, edad):
    return documento == True and edad >= 18

documento = trae_documento()
edad = ingresar_edad()
if puede_pasar(documento, edad):
 print("puede pasar")
else:
    print("No puede pasar")



