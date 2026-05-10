import random

acciones = ["A", "B", "C"]

Q = {
    "A": 10,
    "B": 5,
    "C": 2
}

epsilon = 0.2

for _ in range(20):

    if random.random() < epsilon:

        accion = random.choice(acciones)
        tipo = "Exploración"

    else:

        accion = max(
            acciones,
            key=lambda a: Q[a]
        )

        tipo = "Explotación"

    print(tipo, "->", accion)