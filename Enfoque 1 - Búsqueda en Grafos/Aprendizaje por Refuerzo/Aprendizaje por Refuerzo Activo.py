import random

estados = [0, 1, 2]

acciones = {
    0: [0, 1],
    1: [0, 1],
    2: [0]
}

transiciones = {
    (0,0): 0,
    (0,1): 1,
    (1,0): 0,
    (1,1): 2,
    (2,0): 2
}

recompensas = {
    (0,0): 0,
    (0,1): 1,
    (1,0): 0,
    (1,1): 10,
    (2,0): 10
}

Q = {}

for estado in estados:
    for accion in acciones[estado]:
        Q[(estado, accion)] = 0

alpha = 0.1
gamma = 0.9
epsilon = 0.2

for _ in range(1000):

    estado = 0

    while estado != 2:

        if random.random() < epsilon:
            accion = random.choice(
                acciones[estado]
            )
        else:
            accion = max(
                acciones[estado],
                key=lambda a: Q[(estado,a)]
            )

        siguiente = transiciones[(estado, accion)]

        mejor_q = max(
            [Q[(siguiente,a)]
            for a in acciones[siguiente]]
        )

        Q[(estado, accion)] += alpha * (
            recompensas[(estado, accion)]
            + gamma * mejor_q
            - Q[(estado, accion)]
        )

        estado = siguiente

print("Valores Q:")

for k, v in Q.items():
    print(k, round(v, 2))