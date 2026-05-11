hechos = [
    "llueve"
]

reglas = [
    ("llueve", "trafico"),
    ("trafico", "tarde"),
    ("tarde", "estres")
]

cambio = True

while cambio:

    cambio = False

    for condicion, conclusion in reglas:

        if (
            condicion in hechos
            and conclusion not in hechos
        ):

            hechos.append(conclusion)

            cambio = True

            print(
                "Nueva conclusión:",
                conclusion
            )

print("\nHechos finales:")

for hecho in hechos:
    print("-", hecho)