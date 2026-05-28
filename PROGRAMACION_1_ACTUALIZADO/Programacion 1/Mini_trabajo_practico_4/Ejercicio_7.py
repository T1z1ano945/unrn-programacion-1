# Ejercicio 1 Rankings de ciudades:

registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]

print("-"*60)
ciudades_sin_repetir = set()

for registro in registros:
    ciudades_sin_repetir.add(registro[1])

print(ciudades_sin_repetir)
print("-"*60)

fechas_sin_repetir = set()

for registro in registros:
    fechas_sin_repetir.add(registro[0])

print(fechas_sin_repetir)
print("-"*60)

diccionario_de_fechas = dict(registros)
