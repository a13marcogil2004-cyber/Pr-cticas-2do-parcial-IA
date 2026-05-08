estados = [0, 1, 2]

recompensas = {
    0: 0,
    1: 1,
    2: 10
}

transiciones = {
    0: 1,
    1: 2,
    2: 2
}

gamma = 0.9

utilidades = {
    estado: 0
    for estado in estados
}

for _ in range(20):

    nuevas = utilidades.copy()

    for estado in estados:

        siguiente = transiciones[estado]

        nuevas[estado] = (
            recompensas[estado]
            + gamma * utilidades[siguiente]
        )

    utilidades = nuevas

print("Utilidades aprendidas:")

for estado, valor in utilidades.items():
    print(estado, "->", round(valor, 2))