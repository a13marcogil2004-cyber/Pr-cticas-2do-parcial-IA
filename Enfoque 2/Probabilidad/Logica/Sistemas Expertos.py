hechos = [
    "fiebre",
    "tos"
]

reglas = [
    (
        ["fiebre", "tos"],
        "gripe"
    ),
    (
        ["dolor_cabeza", "fiebre"],
        "migraña"
    )
]

conclusiones = []

for condiciones, conclusion in reglas:

    cumple = True

    for condicion in condiciones:

        if condicion not in hechos:
            cumple = False

    if cumple:

        conclusiones.append(conclusion)

print("Conclusiones:")

for c in conclusiones:
    print("-", c)