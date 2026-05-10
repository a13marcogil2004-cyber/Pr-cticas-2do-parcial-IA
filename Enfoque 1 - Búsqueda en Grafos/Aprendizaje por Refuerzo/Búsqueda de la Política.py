import random

acciones = ["Izquierda", "Derecha"]

politica = {
    "Izquierda": 0.5,
    "Derecha": 0.5
}

for episodio in range(20):

    accion = random.choices(
        acciones,
        weights=[
            politica["Izquierda"],
            politica["Derecha"]
        ]
    )[0]

    if accion == "Derecha":
        recompensa = 1
    else:
        recompensa = 0

    if recompensa == 1:
        politica["Derecha"] += 0.05
        politica["Izquierda"] -= 0.05

    politica["Derecha"] = max(
        0,
        min(1, politica["Derecha"])
    )

    politica["Izquierda"] = 1 - politica["Derecha"]

    print(
        episodio,
        accion,
        recompensa,
        politica
    )