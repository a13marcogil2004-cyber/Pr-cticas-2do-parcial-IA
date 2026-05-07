estados = [0, 1, 2]

recompensas = {
    0: 0,
    1: 1,
    2: 10
}

transiciones = {
    0: [1],
    1: [2],
    2: [2]
}

gamma = 0.9

valores = {
    estado: 0
    for estado in estados
}

for _ in range(20):

    nuevos = valores.copy()

    for estado in estados:

        futuros = []

        for siguiente in transiciones[estado]:

            valor = (
                recompensas[siguiente]
                + gamma * valores[siguiente]
            )

            futuros.append(valor)

        nuevos[estado] = max(futuros)

    valores = nuevos

print("Valores finales:")

for estado, valor in valores.items():
    print(estado, "->", round(valor, 2))