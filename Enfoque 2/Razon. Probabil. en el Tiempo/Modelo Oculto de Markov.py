estados = ["Soleado", "Lluvioso"]

observaciones = ["Caminar", "Paraguas"]

transicion = {
    ("Soleado", "Soleado"): 0.8,
    ("Soleado", "Lluvioso"): 0.2,
    ("Lluvioso", "Soleado"): 0.4,
    ("Lluvioso", "Lluvioso"): 0.6
}

emision = {
    ("Soleado", "Caminar"): 0.7,
    ("Soleado", "Paraguas"): 0.3,
    ("Lluvioso", "Caminar"): 0.2,
    ("Lluvioso", "Paraguas"): 0.8
}

estado_actual = "Soleado"

for t in range(5):

    mejor_estado = None
    mejor_prob = 0

    for siguiente in estados:

        prob = (
            transicion[(estado_actual, siguiente)]
            *
            emision[(siguiente, "Paraguas")]
        )

        if prob > mejor_prob:
            mejor_prob = prob
            mejor_estado = siguiente

    print(
        f"t={t} -> {mejor_estado}"
    )

    estado_actual = mejor_estado