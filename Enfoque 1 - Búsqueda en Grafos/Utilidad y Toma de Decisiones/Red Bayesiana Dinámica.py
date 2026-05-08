estados = ["Soleado", "Lluvioso"]

transicion = {
    ("Soleado", "Soleado"): 0.8,
    ("Soleado", "Lluvioso"): 0.2,
    ("Lluvioso", "Soleado"): 0.4,
    ("Lluvioso", "Lluvioso"): 0.6
}

estado_actual = "Soleado"

for t in range(5):

    probabilidades = []

    for siguiente in estados:

        prob = transicion[(estado_actual, siguiente)]
        probabilidades.append((siguiente, prob))

    siguiente_estado = max(
        probabilidades,
        key=lambda x: x[1]
    )[0]

    print(f"t={t}: {estado_actual}")

    estado_actual = siguiente_estado